from lyricsgenius import Genius
import os
from dotenv import load_dotenv


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

if __name__ == "__main__":
    track = "Blinding Lights"
    artist = "The Weeknd"
    
    genius = initialize_genius()
    lyrics = get_lyrics(genius, track, artist)