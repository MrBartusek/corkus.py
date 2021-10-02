from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional

from .base_server import BaseServer

if TYPE_CHECKING:
    from corkus import Corkus
    from .server import Server

class PartialServer(BaseServer):
    """Represents a ``Partial`` version of :py:class:`Server`."""
    def __init__(self, corkus: Corkus, name: str):
        super().__init__(corkus, name, None)

    async def fetch(self, timeout: Optional[int] = None) -> Union[Server, None]:
        """Fetch full server information from API. Returns ``None`` if server no longer exist.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        online_players = await self._corkus.network.online_players(timeout)
        for server in online_players.servers:
            if server.name == self.name:
                return server
        return None

    def __repr__(self) -> str:
        return f"<PartialServer name={self.name!r}>"
