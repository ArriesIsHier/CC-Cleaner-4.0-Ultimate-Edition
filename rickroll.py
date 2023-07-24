# rickroll.py
import webbrowser as wb
from random import choice
import configparser
import logging
from .media import change_wallpaper, set_volume_max

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

class RickRollException(Exception):
    """
    A custom exception for handling errors related to the Rickroll function.
    If no message is provided, a random rickroll-themed message will be used.
    """
    DEFAULT_MESSAGES = [
        "The code seems to be giving you up",
        "The code's letting you down",
        "If you ask Rick Astley for his copy of the movie Up, he can't give it to you as he is never gonna give you up. But in doing so, he lets you down...",
        "We're no strangers to Python. You know the rules and sO dO i"
    ]

    def __init__(self, message=None):
        if message is None:
            message = choice(self.DEFAULT_MESSAGES)
        super().__init__(message)

def rickroll():
    """
    Opens a YouTube link to the "Never Gonna Give You Up" music video.
    """
    url = config.get('URLS', 'RICK_ROLL')
    try:
        wb.open(url)
    except Exception as err:
        raise RickRollException(f"Failed to open the URL {url}") from err

def rickroll_text(lines=55):
    """
    Returns a specified number of lines from the lyrics of "Never Gonna Give You Up."
    """
    lyrics = """We're no strangers to love
    ...
    Never gonna say goodbye"""  # truncated for brevity

    lyrics_lines = lyrics.split("\n")
    if lines > len(lyrics_lines):
        raise RickRollException("You only wish the song was that long")
    return "\n".join(lyrics_lines[:lines])

def subtle_rickroll():
    """
    Opens a random YouTube link from a list, presumably all different versions or remixes of "Never Gonna Give You Up."
    """
    urls = config.get('URLS', 'SUBTLE_RICK_ROLLS').split(', ')
    url = choice(urls)
    try:
        wb.open(url)
    except Exception as err:
        raise RickRollException(f"Failed to open the URL {url}") from err

def ultimate_rickroll():
    """
    Changes the wallpaper, sets the volume to maximum, and opens the YouTube link to "Never Gonna Give You Up."
    """
    wallpaper_path = config.get('PATHS', 'WALLPAPER')
    try:
        # Change the wallpaper
        change_wallpaper(wallpaper_path)

        # Set the volume to max and unmute
        set_volume_max()

        # Open the classic Rickroll
        rickroll()
    except Exception as err:
        raise RickRollException("Failed to perform the ultimate rickroll") from err
