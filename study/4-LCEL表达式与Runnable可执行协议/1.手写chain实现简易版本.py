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


# 2. 定义一个链子
@dataclass
class Chain:
    steps: list

    def invoke(self, input: Any) -> Any:
        temp = input
        for step in self.steps:
            temp = step.invoke(temp)
            print("步骤: ", step)
            print("结果: ", temp)
            print("============")
        return input


# 3. 编排
chain = Chain([prompt_template, llm, parser])
# 4. 结果
print(chain.invoke({"query": "你好，你是？"}))
