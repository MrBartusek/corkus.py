from __future__ import annotations
from enum import Enum

from .base import CorkusBase
from .uuid import CorkusUUID

class PlayerRank(Enum):
    """Player special rank."""
    ADMINISTRATOR = "Administrator"
    """Admins are either the owners or developers of Wynncraft."""

    MODERATOR = "Moderator"
    """Moderators enforce the Wynncraft rules on the forums, game servers, and Discord.
    They are also here to help players when needed."""

    BUILDER = "Builder"
    """The Builder tag is given to the builders who built the physical map."""

    ITEM = "Item"
    """Members of the Item Team create new items as well as balance existing ones."""

    GAME_MASTER = "Game Master"
    """The GM tag is given to Game Masters, the creators of items, quests, mobs, etc."""

    CMD = "CMD"
    """The CMD tag is given to the talented command blockers who create the cutscenes and
    puzzle you see in-game."""

    MUSIC = "Music"
    """Given to the official composers of Wynncraft's music."""


    HYBRID = "Hybrid"
    """The Hybrid tag is given to Wynncraft Hybrids; Content Team members who are both builders, GMs, or CMDs."""

    MEDIA = "Media"
    """Media is granted to those who record and post Wynncraft videos on Youtube or stream Wynncraft."""

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
        """Player special rank, if don't have one, default to :py:attr:`PlayerRank.PLAYER`."""
        return PlayerRank(self._attributes.get("rank", PlayerRank.PLAYER))

    @property
    def tag(self) -> PlayerTag:
        """Player's rank bought from `Wynncraft Store <https://store.wynncraft.com>`_."""
        return PlayerTag(self._attributes.get("meta", {}).get("tag", {}).get("value", PlayerTag.PLAYER))

    @property
    def veteran(self) -> bool:
        """Is player a veteran, meaning, had VIP before August 1, 2014 which was when the 1.12 update was
        released and Minecraft EULA changed.
        """
        return self._attributes.get("meta", {}).get("veteran", False)

    def __repr__(self) -> str:
        return f"<BasePlayer uuid={self.uuid!r}>"
