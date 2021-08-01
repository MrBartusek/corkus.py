from enum import Enum
from typing import Union

class PlaytimeConvertRatio(Enum):
    """Most popular playtime convertion ratios

    OFFICIAL - 4.7 ratio used by official wynncraft statistics page
    WYNNDATA - 5.0 ratio used by wynndata.tk
    """
    RAW = 1
    OFFICIAL = 4.7
    WYNNDATA = 5

class PlayerPlaytime():
    """Object that helps to convert playtime

    Wynncraft API returns player playtime in wired way and it can't be used directly.
    See https://github.com/Wynncraft/WynncraftAPI/issues/8

    To get most popular conversion ratios see PlaytimeConvertRatio Enum
    """

    def __init__(self, playtime: int) -> None:
        self._playtime = playtime

    @property
    def raw(self) -> int:
        """Get number that API returned"""
        return self._playtime

    def minutes(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        """Convert time using specified ratio and return it as minutes"""
        return self._convert(ratio)

    def hours(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        """Convert time using specified ratio and return it as hours"""
        return self._convert(ratio) / 60

    def _convert(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        if isinstance(ratio, PlaytimeConvertRatio):
            ratio = ratio.value
        return round(self._playtime * ratio)
