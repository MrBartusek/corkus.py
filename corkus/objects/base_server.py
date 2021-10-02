from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum

from .base import CorkusBase

if TYPE_CHECKING:
    from corkus import Corkus

class ServerType(Enum):
    """Type of :py:class:`Server`."""
    REGULAR = "WC"
    """Regular Wynncraft servers."""

    YOUTUBE = "YT"
    """Servers restricted to players with :py:attr:`PlayerRank.MEDIA` rank."""

class BaseServer(CorkusBase):
    def __init__(self, corkus: Corkus, name: str, attributes: dict = None):
        self._name = name
        if attributes is None:
            attributes = []
        super().__init__(corkus, attributes)

    @property
    def name(self) -> str:
        """The name of server like ``WC1`` or ``WC16`` or ``YT``."""
        return self._name

    @property
    def type(self) -> ServerType:
        """Type of the server."""
        return ServerType("".join([i for i in self.name if not i.isdigit()]))

    @property
    def regular(self) -> bool:
        """Is this a regular server (:py:attr:`type` is :py:attr:`ServerType.REGULAR`)."""
        return self.type == ServerType.REGULAR
