from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain

def qa_agent(dashscope_api_key, memory, uploader_file, question):
    model = ChatTongyi(model="qwen-max", dashscope_api_key=dashscope_api_key)

    # 数据源
    file_content = uploader_file.read() # 将用户上传的文件读取为一个字符串
    temp_file_path = "temp.pdf" # 为一个临时文件指定路径和文件名
    with open(temp_file_path, "wb") as f:
        f.write(file_content)

    # 加载
    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()

    # 分割
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n", "。", "！", "？", "，", "、", ""]
    )
    texts = text_splitter.split_documents(docs)

    # 嵌入
    embeddings_model = DashScopeEmbeddings(
        model="text-embedding-v1",
        dashscope_api_key=dashscope_api_key
    )

    # 储存
    db = FAISS.from_documents(texts, embeddings_model)
    retriever = db.as_retriever()

    # 检索
    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        memory=memory,
        retriever=retriever
    )
    response = qa.invoke({"chat_history": memory, "question": question})
    return response