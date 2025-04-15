from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()


model = ChatOpenAI(model='gpt-4',temperature=0.5,max_completion_tokens=10)

result = model.invoke('Who is the president of India')

# print(result)
print(result.content)