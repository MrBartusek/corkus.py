from corkus.objects import partial_base
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
