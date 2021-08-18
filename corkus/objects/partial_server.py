from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional

from .partial_base import PartialBase
from .server import ServerType

if TYPE_CHECKING:
    from corkus import Corkus
    from .server import Server

class PartialServer(PartialBase):
    """Represents a ``Partial`` version of :py:class:`Server`."""
    def __init__(self, corkus: Corkus, name: str):
        super().__init__(corkus)
        self._name = name

    @property
    def name(self) -> str:
        """The name of server."""
        return self._name

    @property
    def type(self) -> ServerType:
        """Type of the server, most servers are stanard servers."""
        return ServerType("".join([i for i in self._name if not i.isdigit()]))

    async def fetch(self, timeout: Optional[int] = None) -> Union[Server, None]:
        """Fetch full server information from API. Returns ``None`` if server no longer exist.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        servers = await self.corkus.network.servers_list(timeout)
        for server in servers:
            if server.name == self.name:
                return server
        return None

    def __repr__(self) -> str:
        return f"<PartialServer name={self.name!r}>"
