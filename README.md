测试版本为python-3.10
# 简介
一个基于大模型与检索增强生成（RAG）技术的 PDF 智能问答工具，支持上传 PDF 文档并通过自然语言进行多轮对话式提问，快速提取文档关键信息。

# 功能特点
<br>📄 PDF 解析：支持上传 PDF 文件，自动加载并解析文档内容</br>
<br>🤖 智能问答：基于通义千问大模型（qwen-max），结合文档内容生成精准回答</br>
<br>🔄 多轮对话：支持上下文记忆，可进行连续对话交互</br>
<br>🔍 精准检索：通过向量数据库（FAISS）实现文档内容高效检索，提升回答相关性</br>
<br>🖥️ 简洁界面：基于 Streamlit 构建直观易用的交互界面</br>

# 技术栈
<br>大模型：通义千问（qwen-max）、DashScope Embeddings</br>
<br>框架工具：LangChain（文档处理、对话链构建）、Streamlit（前端界面）</br>
<br>数据处理：PyPDFLoader（PDF 解析）、RecursiveCharacterTextSplitter（文本分块）</br>
<br>向量存储：FAISS（高效向量检索）</br>
<br>对话记忆：ConversationBufferMemory（上下文管理）</br>

# 待优化方向
<br>支持多文件上传与批量处理</br>
<br>增加文档内容预览功能</br>
<br>优化大文件处理效率</br>
<br>支持更多文档格式（Word、TXT 等）</br>
<br>增加模型选择功能（支持多模型切换）</br>
