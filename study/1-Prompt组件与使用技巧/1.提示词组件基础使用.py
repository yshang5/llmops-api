"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import AIMessage
from datetime import datetime

# 单轮 PromptTemplate：只做变量替换，输出仍然是一段普通文本。
prompt = PromptTemplate.from_template("请将一个关于{language}程序员的冷笑话")
print(prompt.format(language="java"))
prompt_value = prompt.invoke({"language": "java"})
print(prompt_value.to_string())
print(prompt_value.to_messages())

# ChatPromptTemplate 用来组织多轮消息：
# system 负责设定角色，chat_history 插入历史对话，最后一条 human 是当前用户输入。
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是OpenAI开发的聊天机器人，请根据用户的回答进行回复，当前时间为:{now}"),
        # 把 invoke 时传入的 chat_history 原样插入到这里。
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template("请将一个关于{language}程序员的冷笑话")
    ]
    # partial 提前绑定模板变量；这里传入 datetime.now 函数本身，
    # 所以每次 invoke 时都会重新获取一次当前时间。
).partial(now=datetime.now)
chat_prompt_value = chat_prompt_template.invoke(
    input={
        "language": "java",
        "chat_history": [
            # 在 LangChain 里，human/ai 会映射成底层模型常见的 user/assistant。
            ("human", "你好啊"),
            AIMessage("你好，我是你的AI助手，有什么可以帮助您")
        ]
    }
)
print(chat_prompt_value)
print("-------------------------")
print(chat_prompt_value.to_messages())
print(chat_prompt_value.to_string())
