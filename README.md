测试版本为python-3.10
# 简介
一个基于大模型与检索增强生成（RAG）技术的 PDF 智能问答工具，支持上传 PDF 文档并通过自然语言进行多轮对话式提问，快速提取文档关键信息。

# 功能特点
📄 PDF 解析：支持上传 PDF 文件，自动加载并解析文档内容
🤖 智能问答：基于通义千问大模型（qwen-max），结合文档内容生成精准回答
🔄 多轮对话：支持上下文记忆，可进行连续对话交互
🔍 精准检索：通过向量数据库（FAISS）实现文档内容高效检索，提升回答相关性
🖥️ 简洁界面：基于 Streamlit 构建直观易用的交互界面

# 技术栈
大模型：通义千问（qwen-max）、DashScope Embeddings
框架工具：LangChain（文档处理、对话链构建）、Streamlit（前端界面）
数据处理：PyPDFLoader（PDF 解析）、RecursiveCharacterTextSplitter（文本分块）
向量存储：FAISS（高效向量检索）
对话记忆：ConversationBufferMemory（上下文管理）
