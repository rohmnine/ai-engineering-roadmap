from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("请在.env文件中设置OPENAI_API_KEY环境变量")
    exit()

client = OpenAI(
    api_key=api_key
)

user_input = input("请输入你的问题：")

try:
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=user_input
    )
except Exception as e:
    print("请求失败，请检查网络连接或API Key是否正确。错误信息：", e)


#     response = client.responses.create(
#         model="gpt-5.4-mini",
#         instructions="""你是一名Python老师,
#         帮助我学习Python编程语言,请使用简单易懂的语言回答问题,
#         回答的字数控制在200字以内。
#         面向Python初学者解释。""",
#         input=user_input
#     )

# 练习二：输出字数限制
#    answer = response.output_text
#     answer = answer[:10]
#     print(answer)

print(
        "AI:",
        response.output_text
    ) 