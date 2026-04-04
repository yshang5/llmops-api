"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
from langchain_core.prompts import ChatPromptTemplate

system_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是个机器人, 名字叫{name}"),
    ]
)

human_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{query}")
    ]
)
chat_prompt = system_prompt + human_prompt
print(chat_prompt.invoke({"query": "你好啊", "name": "虾仁"}))
