from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model  = ChatOpenAI(model='gpt-4o',temperature=0)

result = model.invoke('Write a 5 line peom on cricket')

print(result.content)
