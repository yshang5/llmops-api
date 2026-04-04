"""
  @File    : conftest.py.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
from langchain_core.prompts import PromptTemplate

full_template = PromptTemplate.from_template("""{instruction}

{example}

{start}
""")

# 描述模板
instruction_template = PromptTemplate.from_template("你正在模拟{person}")

# 示例模板
example_template = PromptTemplate.from_template("""下面是一个交互例子：
Q: {example_q}
A: {example_a}
""")

# 开始模板
start_prompt = PromptTemplate.from_template("""现在你是个真是的人,请回答用户问题：
Q: {input}
A: 
""")

composed_template_str = full_template.format(
    instruction=instruction_template.template,
    example=example_template.template,
    start=start_prompt.template,
)

final_prompt = PromptTemplate.from_template(composed_template_str)
print(final_prompt)

print(
    final_prompt.invoke(
        {
            "person": "马斯克",
            "example_q": "你最喜欢什么车？",
            "example_a": "Tesla",
            "input": "你最喜欢哪个社交平台？",
        }

    ).to_string()
)
