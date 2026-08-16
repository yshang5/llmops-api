"""
  @File    : vector_database_service.py
  @Author  : Yue
  @Date    : 2026/4/18 20:26
  @Desc    : 
"""
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import OpenAIEmbeddings
from langchain_weaviate import WeaviateVectorStore
from injector import inject
from weaviate import WeaviateClient
import weaviate
import os


@inject
class VectorDatabaseService:
    """向量数据库服务"""
    vector_stores: WeaviateVectorStore
    client: WeaviateClient

    def __init__(self):
        """初始化，完成weaviate客户端和langchain向量数据库实例创建"""
        self.client = weaviate.connect_to_local(host=os.getenv("WEAVIATE_HOST"), port=int(os.getenv("WEAVIATE_PORT")))
        self.vector_stores = WeaviateVectorStore(
            client=self.client,
            index_name="Dataset",
            text_key="text",
            embedding=OpenAIEmbeddings(
                base_url=os.getenv("APP_OPENAI_BASE_URL"),
                api_key=os.getenv("APP_OPENAI_API_KEY"),
                model="text-embedding-3-small",
            )
        )

    @classmethod
    def combine_documents(cls, documents: list[Document]) -> str:
        """将对应的文本列表使用换行符进行合并"""
        return "\n\n".join([document.page_content for document in documents])

    def get_retriever(self) -> VectorStoreRetriever:
        return self.vector_stores.as_retriever()
