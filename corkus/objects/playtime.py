from __future__ import annotations
from enum import Enum
from typing import Union

class PlaytimeConvertRatio(Enum):
    """Most popular playtime convertion ratios."""

    RAW = 1.0
    """1.0 value returned by the API."""

    OFFICIAL = 4.7
    """4.7 ratio used by official wynncraft statistics page."""

    WYNNDATA = 5
    """5.0 ratio used by `Wynndata <https://www.wynndata.tk/>`_."""

class PlayerPlaytime():
    """Object that helps to convert playtime

    Wynncraft API returns player playtime in wired way and it can't be used directly.
    See `Wynncraft/WynncraftAPI#8 <https://github.com/Wynncraft/WynncraftAPI/issues/8>`_

    To get most popular conversion ratios see :py:class:`PlaytimeConvertRatio` Enum.
    """
    def __init__(self, playtime: int) -> None:
        self._playtime = playtime

    @property
    def raw(self) -> int:
        """Get number that API returned."""
        return self._playtime

    def seconds(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        """Convert time using specified ratio and return it as seconds.

        :param ratio: Ratio by which raw playtime will be multiplied.
        """
        return self._convert(ratio) * 60

    def minutes(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        """Convert time using specified ratio and return it as minutes.

        :param ratio: Ratio by which raw playtime will be multiplied.
        """
        return self._convert(ratio)

    def hours(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        """Convert time using specified ratio and return it as hours.

        :param ratio: Ratio by which raw playtime will be multiplied.
        """
        return self._convert(ratio) / 60

    def _convert(self, ratio: Union[PlaytimeConvertRatio, float]) -> int:
        if isinstance(ratio, PlaytimeConvertRatio):
            ratio = ratio.value
        return round(self._playtime * ratio)
