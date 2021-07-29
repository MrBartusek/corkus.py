from enum import Enum
from .base import CorkusBase
from .uuid import CorkusUUID

class PlayerRank(Enum):
    """ Player Wynncraft Team Rank, if not in content team defaults to PLAYER """

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

class Player(CorkusBase):
    @property
    def username(self) -> int:
        return self.attributes.get("username")

    @property
    def uuid(self) -> CorkusUUID:
        return CorkusUUID(self.attributes.get("uuid"))

    @property
    def rank(self) -> PlayerRank:
        return PlayerRank(self.attributes.get("rank", PlayerRank.PLAYER))

    @property
    def in_content_team(self) -> bool:
        return self.rank != PlayerRank.PLAYER
