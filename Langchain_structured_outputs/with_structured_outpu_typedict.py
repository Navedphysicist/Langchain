from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

class player_deails(TypedDict):
    name : str
    sport : Annotated[str,"Write the Sport details of the player"]
    summary: Annotated[str, "A brief summary of the Information"]
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    good_things : Annotated[Optional[list[str]], "Write down all the good things about the player in  a list"]
    bad_things : Annotated[Optional[list[str]], "Write down all the bad things about the player in  a list"]



structured_model = model.with_structured_output(player_deails)
output = structured_model.invoke("""Virat Kohli is a famous Indian cricketer, born on November 5, 1988, in Delhi. He is known for being one of the best batsmen in the world. He has scored many runs and won several awards. Kohli was also the captain of the Indian cricket team for many years and helped the team win important matches.

People admire him for his hard work, fitness, and passion for the game. He brought new energy to Indian cricket and inspired many young players.

However, Kohli has also faced some problems. In recent years, his performance has gone down. He hasn't scored as many runs as before. Some people also say he was too aggressive on the field and made too many changes in the team during his captaincy. Even with these challenges, he is still loved by millions and continues to be a big name in cricket.
                                 """)

print(output)

