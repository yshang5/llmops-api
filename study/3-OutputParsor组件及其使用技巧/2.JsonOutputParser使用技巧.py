"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
import dotenv
import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

dotenv.load_dotenv()


# 创建一个json数据结构 用于告诉大语言模型这个json结构长什么样子的

class Joke(BaseModel):
    joke: str = Field(description="回复给用户的冷笑话")
    punchline: str = Field(description="这个冷笑话的笑点")


parser = JsonOutputParser(pydantic_object=Joke)

# 创建一个提示词模板
prompt = ChatPromptTemplate.from_template("""请根据用户的提问回答: 
{instruction} 
{query}
""").partial(instruction=parser.get_format_instructions())

llm = ChatOpenAI(
    base_url=os.getenv("APP_OPENAI_BASE_URL"),
    api_key=os.getenv("APP_OPENAI_API_KEY"),
    model="gpt-5.4-nano"
)
result = parser.invoke(llm.invoke(prompt.invoke("请将一个程序员的冷笑话")))
print(result)
