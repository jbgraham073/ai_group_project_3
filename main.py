from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lyricsgenius import Genius
from langchain_openai import ChatOpenAI
import gradio as gr
from dotenv import load_dotenv
import os


def initialize_genius():
    """
    Initializes the Genius object with the necessary API key and settings.
    
    Returns:
    - genius: The initialized Genius object.
    """
    load_dotenv()
    GENIUS_API_KEY = os.getenv('GENIUS_API_KEY')

    genius = Genius(
        access_token=GENIUS_API_KEY,
        timeout=15,
        sleep_time=1,
        verbose=False,
        remove_section_headers=True,
        skip_non_songs=True,
        excluded_terms=["(Remix)", "(Live)", "You might also like", "Embed"],
        retries=3
    )
    
    return genius

def tidy_lyrics(lyrics):
    """
    Cleans up the lyrics by removing unnecessary sections and characters.
    
    Args:
    - lyrics: The lyrics to be tidied.
    
    Returns:
    - The tidied lyrics.
    """
    if lyrics.find('Lyrics') != -1:
        lyrics = lyrics[(lyrics.find('Lyrics')+len('Lyrics')):]

    if lyrics[-5:] == 'Embed':
        lyrics = lyrics[:-5]

    lyrics = lyrics.replace('You might also like', '')
    lyrics = lyrics.replace(';', '')
    

    while lyrics[-1].isdigit():
        lyrics = lyrics[:-1]
        
    return lyrics     

def get_lyrics(genius, track, artist, tidy=True):
    """
    Retrieves the lyrics of a given track by a specific artist.

    Parameters:
    - track (str): The title of the track.
    - artist (str): The name of the artist.
    - tidy (bool, optional): Whether to tidy up the lyrics by removing unnecessary characters. Defaults to True.

    Returns:
    - lyrics (str or None): The lyrics of the track, or None if the lyrics couldn't be found.

    """
    try:
        song = genius.search_song(track, artist, get_full_info=False)
    
        if song is None:
            lyrics = None
        else:
            if tidy:
                lyrics = tidy_lyrics(song.lyrics)
            else:
                lyrics = song.lyrics
    except:
        lyrics = None
    
    return lyrics

def vader_song_sentiment(lyrics):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(lyrics)
    
    return sentiment_scores

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

def search_analyze_song(song_title, song_artist):
    genius = initialize_genius()
    lyrics = get_lyrics(genius, song_title, song_artist)

    vader_sent = vader_song_sentiment(lyrics)
    
    return(lyrics, vader_sent['pos'], vader_sent['neg'], vader_sent['neu'], vader_sent['compound'])

def sent_swap(new_sentiment, lyrics):
    gpt_sent = gpt_sent_shift(lyrics, new_sentiment)
    new_vader_sent = vader_song_sentiment(gpt_sent)
    return(gpt_sent_shift(lyrics, new_sentiment), new_vader_sent['pos'], new_vader_sent['neg'], new_vader_sent['neu'], new_vader_sent['compound'])


with gr.Blocks() as app:
    with gr.Row():
        with gr.Column():
            with gr.Group():
                song_title = gr.Textbox(lines=1, label="Song Title")
                song_artist = gr.Textbox(lines=1, label="Song Artist")
                search = gr.Button(value="Search")    
            song_lyrics = gr.Textbox(lines=10, label="Lyrics")
            with gr.Row():
                pos = gr.Textbox(lines=1, label="Positive")
                neg = gr.Textbox(lines=1, label="Negative")
                neu = gr.Textbox(lines=1, label="Neutral")
                com = gr.Textbox(lines=1, label="Compound")
            search.click(fn=search_analyze_song, inputs=[song_title, song_artist], outputs=[song_lyrics, pos, neg, neu, com])
        with gr.Column():
            with gr.Group():
                new_sentiment = gr.Textbox(lines=1, label="Sentiment", scale=2)
                submit = gr.Button(value="Submit")
            new_lyrics = gr.Textbox(lines=10, label="Lyrics")
            with gr.Row():
                pos = gr.Textbox(lines=1, label="Positive")
                neg = gr.Textbox(lines=1, label="Negative")
                neu = gr.Textbox(lines=1, label="Neutral")
                com = gr.Textbox(lines=1, label="Compound")
            submit.click(fn=sent_swap, inputs=[new_sentiment, song_lyrics], outputs=[new_lyrics, pos, neg, neu, com])
    

app.launch(share=True)

