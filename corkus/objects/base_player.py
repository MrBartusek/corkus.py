from __future__ import annotations
from enum import Enum

from .base import CorkusBase
from .uuid import CorkusUUID
from corkus.utils import CorkusEnum

class PlayerRank(Enum):
    """Player special rank."""
    ADMINISTRATOR = "ADMINISTRATOR"
    """Admins are either the owners or developers of Wynncraft."""

    MODERATOR = "MODERATOR"
    """Moderators enforce the Wynncraft rules on the forums, game servers, and Discord.
    They are also here to help players when needed."""

    BUILDER = "BUILDER"
    """The Builder tag is given to the builders who built the physical map."""

    ITEM = "ITEM"
    """Members of the Item Team create new items as well as balance existing ones."""

    GAME_MASTER = "GAME_MASTER"
    """The GM tag is given to Game Masters, the creators of items, quests, mobs, etc."""

    CMD = "CMD"
    """The CMD tag is given to the talented command blockers who create the cutscenes and
    puzzle you see in-game."""

    MUSIC = "MUSIC"
    """Given to the official composers of Wynncraft's music."""

    HYBRID = "HYBRID"
    """The Hybrid tag is given to Wynncraft Hybrids; Content Team members who are both builders, GMs, or CMDs."""

    MEDIA = "MEDIA"
    """Media is granted to those who record and post Wynncraft videos on Youtube or stream Wynncraft."""

    REGULAR = "REGULAR"

class PlayerTag(CorkusEnum):
    """Player's rank bought from `Wynncraft Store <https://store.wynncraft.com>`_."""
    CHAMPION = "CHAMPION"
    HERO = "HERO"
    VIP_PLUS = "VIP+"
    VIP = "VIP"
    PLAYER = "PLAYER"

class BasePlayer(CorkusBase):
    @property
    def uuid(self) -> CorkusUUID:
        """Minecraft UUID of player."""
        return CorkusUUID(self._attributes.get("uuid", ""))

    @property
    def rank(self) -> PlayerRank:
        """Player special rank, if don't have one, default to :py:attr:`PlayerRank.REGULAR`."""
        rank = self._attributes.get("rank")
        if rank is None or rank.upper() == "PLAYER":
            rank = "REGULAR"
        return PlayerRank(rank.upper().replace(" ", "_"))

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
