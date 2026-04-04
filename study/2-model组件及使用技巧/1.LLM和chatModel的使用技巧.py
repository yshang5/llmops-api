"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
import json

import dotenv
import os
from datetime import datetime
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.base import message_to_dict

dotenv.load_dotenv()

# 1. 编排prompt
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是OpenAI开发的聊天机器人，现在时间是{now}，请回答用户问题"),
        ("human", "{query}")
    ]
).partial(now=datetime.now)

# 2. 创建打语音模型
llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-5.4-nano"
)
# 3. 调用
ai_message = llm.invoke(prompt_template.invoke(
    {"query": "现在是几点？请将一个关于java程序员的冷笑话"}
))
print(json.dumps(message_to_dict(ai_message), indent=2))
