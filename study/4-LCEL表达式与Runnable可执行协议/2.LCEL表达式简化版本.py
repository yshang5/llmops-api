"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
from typing import Any

import dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dataclasses import dataclass

dotenv.load_dotenv()

# 1. 构建组件
llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-3.5-turbo"
)
prompt_template = ChatPromptTemplate.from_template("{query}")
parser = StrOutputParser()

# 2. 编排 这些个组件都是runnable, 他们的__or__方法被改写，可以通过竖线来组装编排
chain = prompt_template | llm | parser
# 3. 调用
print(chain.invoke({"query": "你好，你是？"}))
