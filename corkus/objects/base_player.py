from __future__ import annotations
from enum import Enum

from .base import CorkusBase
from .uuid import CorkusUUID

class PlayerRank(Enum):
    """Player Wynncraft Team Rank, if not in content team defaults to :py:attr:`PlayerRank.PLAYER`."""
    ADMINISTRATOR = "Administrator"
    MODERATOR = "Moderator"
    BUILDER = "Builder"
    ITEM = "Item"
    GAME_MASTER = "Game Master"
    CMD = "CMD"
    MUSIC = "Music"
    HYBRID = "Hybrid"
    MEDIA = "Media"
    PLAYER = "Player"

class PlayerTag(Enum):
    """Player's rank bought from `Wynncraft Store <https://store.wynncraft.com>`_."""
    PLAYER = "PLAYER"
    VIP = "VIP"
    VIP_PLUS = "VIP+"
    HERO = "HERO"
    CHAMPION = "CHAMPION"

class BasePlayer(CorkusBase):
    @property
    def uuid(self) -> CorkusUUID:
        """Minecraft UUID of player."""
        return CorkusUUID(self._attributes.get("uuid", ""))

    @property
    def rank(self) -> PlayerRank:
        """Player Wynncraft Team Rank, if not in content team defaults to :py:attr:`PlayerRank.PLAYER`."""
        return PlayerRank(self._attributes.get("rank", PlayerRank.PLAYER))

    @property
    def tag(self) -> PlayerTag:
        """Player's rank bought from `Wynncraft Store <https://store.wynncraft.com>`_."""
        return PlayerTag(self._attributes.get("meta", {}).get("tag", {}).get("value", PlayerTag.PLAYER))

    @property
    def veteran(self) -> bool:
        "Is player a veteran, meaning, had VIP before August 1, 2014 which was when the 1.12 update was released and Minecraft EULA changed."
        return self._attributes.get("meta", {}).get("veteran", False)

    def __repr__(self) -> str:
        return f"<BasePlayer uuid={self.uuid!r}>"
