"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
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
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

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
    return "用户就是大老师"


parser = StrOutputParser()
# on_end 接收的是 RunTree 对象，需要通过 .outputs 获取实际返回值
prompt_with_listener = prompt_template.with_listeners(
    on_end=lambda run_tree: print("📝 Prompt输出:", run_tree.outputs["output"].to_string())
)
chain = RunnablePassthrough.assign(
    context=RunnableLambda(lambda x: retrieval(x["query"]))
) | prompt_with_listener | llm | parser
content = chain.invoke({"query ": "你好， 我是谁"})
print(content)
