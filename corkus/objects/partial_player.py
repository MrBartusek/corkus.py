from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union

from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .player import Player

class PartialPlayer(PartialBase):
    def __init__(self, corkus: Corkus, *, uuid: Optional[CorkusUUID] = None, username: Optional[str] = None):
        super().__init__(corkus)
        self._uuid = uuid
        self._username = username
        if uuid is None and username is None:
            raise ValueError("uuid and username are both none")

    @property
    def username(self) -> Union[str, None]:
        """Minecraft username of player"""
        return self._username

    @property
    def uuid(self) -> Union[CorkusUUID, None]:
        """Minecraft UUID of player"""
        return self._uuid

    async def fetch(self) -> Player:
        """Fetch player data of this member from API"""
        identifier = self._uuid if self._uuid is not None else self._username
        return await self.corkus.player.get(identifier)

    def __repr__(self) -> str:
        result = "<PartialPlayer"
        if self._uuid is not None:
            result += f" uuid={self._uuid.string()!r}"
        if self._username is not None:
            result += f" username={self._username!r}"
        return result + ">"
