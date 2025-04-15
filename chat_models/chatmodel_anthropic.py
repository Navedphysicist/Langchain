#Don't have the Anthropic API_KEY

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('Who is the president of India')

print(result.content)

