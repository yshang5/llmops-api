"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
from langchain_core.prompts import PromptTemplate

prompt = (
        PromptTemplate.from_template("请将一个关于{subject}程序员的冷笑话") +
        ",讲一个让我开心一下, 使用{language}"
)
print(prompt.invoke({"subject": "java", "language": "Chinese"}).to_string())
