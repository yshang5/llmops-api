"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
import dotenv
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()
parser = StrOutputParser()
# 直接parse StrOutputParser会原封不动地返回
parsed = parser.parse(text="程序员梦工厂")
print(parsed)
# 1. 创建打语音模型
llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-5.4-nano"
)
prompt_template = ChatPromptTemplate.from_template("{query}")
content = parser.invoke(llm.invoke(prompt_template.invoke({"query": "你好，你是？"})))
print(content)
