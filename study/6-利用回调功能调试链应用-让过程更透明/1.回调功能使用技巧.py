"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
from datetime import datetime
from typing import Any
from uuid import UUID

import dotenv
import os

from langchain_core.messages import BaseMessage
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk, LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableConfig
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler

dotenv.load_dotenv()


class LLMOpsCallbackHandler(BaseCallbackHandler):
    """自动以LLMOps回调处理器"""
    start_at: float = 0

    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> Any:
        print("聊天模型开始执行了")
        print("serialized: ", serialized)
        print("messages: ", messages)
        print("metadata: ", metadata)
        self.start_at = datetime.now().timestamp()

    # def on_llm_new_token(
    #         self,
    #         token: str,
    #         *,
    #         chunk: GenerationChunk | ChatGenerationChunk | None = None,
    #         run_id: UUID,
    #         parent_run_id: UUID | None = None,
    #         tags: list[str] | None = None,
    #         **kwargs: Any,
    # ) -> Any:
    #     print("token生成了")
    #     print("token: ", token)

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            **kwargs: Any,
    ) -> Any:
        end_at: float = datetime.now().timestamp()
        print("时间消耗: ", end_at - self.start_at)
        print("response: ", response)


llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-5.4-nano"
)

prompt_template = ChatPromptTemplate.from_template("{query}")

chain = RunnableParallel({"query": RunnablePassthrough()}) | prompt_template | llm | StrOutputParser()

content = chain.stream("你好，你是？",
                       config=RunnableConfig(callbacks=[LLMOpsCallbackHandler(), StdOutCallbackHandler()]))

# print(content)
for chunk in content:
    pass
