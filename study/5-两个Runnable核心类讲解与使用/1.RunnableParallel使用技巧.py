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

dotenv.load_dotenv()
# 1. 构建组件
llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-5.4-nano"
)
joke_template = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
poem_template = ChatPromptTemplate.from_template("请写一篇关于{subject}的诗")
parser = StrOutputParser()

joke_chain = joke_template | llm | parser
poem_chain = poem_template | llm | parser

# 并行链 (以下两种，字典，键值对，都行)
map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
# map_chain = RunnableParallel(
#     {
#         "joke": joke_chain,
#         "poem": poem_chain,
#     }
# )
res = map_chain.invoke({"subject": "程序员"})
print(res)
