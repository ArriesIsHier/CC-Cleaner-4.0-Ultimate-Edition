# media.py
import ctypes
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def change_wallpaper(path):
    """
    Changes the wallpaper of the computer to the image at the specified path.
    """
    logger.info(f'Changing wallpaper to image at path {path}...')
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

def set_volume_max():
    """
    Unmutes the computer and sets the volume to maximum.
    """
    logger.info('Setting volume to maximum and unmuting...')
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if volume.GetMute() == 1:
            volume.SetMute(0, None)
        volume.SetMasterVolume(1.0, None)  # 1.0 is the max volume
