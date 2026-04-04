"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
import dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from tenacity import sleep

dotenv.load_dotenv()

# 1. 编排prompt
prompt_template = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行生成。

<context>
{context}
</context>

用户的提问是：{query}
""")
llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-5.4-nano"
)


def retrieval(query: str) -> str:
    print("正在检索...", query)
    sleep(2)
    return "我是大老师"


parser = StrOutputParser()
chain = RunnableParallel(
    {
        "query": lambda x: x["query"],
        "context": lambda x: retrieval(x["query"]),
    }
) | prompt_template | llm | parser
content = chain.invoke({"query": "你好， 我是谁"})
print(content)
