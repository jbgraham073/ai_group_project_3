from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


def gpt_sent_shift(lyrics, user_preference):
    load_dotenv()

    OPENAI_MODEL = "gpt-3.5-turbo"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Load the GPT-3.5-turbo model.
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, temperature=0.2)

    # Generate a song based on the lyrics and user preference.
    query = f'You are a master song writer. Your sense for the meaning of songs and the sentiments they imply is impeccable. I need you to rework the following lyrics and imbue them with a {user_preference} sentiment.  Here are the lyrics: {lyrics}'
    result = llm.invoke(query)

    return(result.content)

if __name__ == "__main__":
    song_lyrics = "Look at the stars. look how they shine for you"
    user_preference = "happy, surprising, and exciting"
    print(gpt_sent_shift(song_lyrics, user_preference))