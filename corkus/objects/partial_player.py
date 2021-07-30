from typing import Optional
from .uuid import CorkusUUID
from .player import Player
from .partial_base import PartialBase

class PartialPlayer(PartialBase):
    def __init__(self, corkus, *, uuid: Optional[CorkusUUID] = None, username: Optional[str] = None):
        super().__init__(corkus)
        self.uuid = uuid
        self.username = username
        if uuid is None and username is None:
            raise ValueError("uuid and username are both none")

    async def fetch(self) -> Player:
        identifier = self.uuid if self.uuid is not None else self.username
        return await self.corkus.player.get(identifier)

    def __repr__(self) -> str:
        result = "<PartialPlayer"
        if self.uuid is not None:
            result += f" uuid={self.uuid.string()!r}"
        if self.username is not None:
            result += f" username={self.username!r}"
        return result + ">"
