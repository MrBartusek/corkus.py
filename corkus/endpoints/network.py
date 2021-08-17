from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import Server

class NetworkEndpoint(Endpoint):
    async def players_sum(self, timeout: Optional[int] = None) -> int:
        """Get number of online players across all servers.

        :param timeout: Optionally override default timeout."""
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "onlinePlayersSum",
            timeout = timeout
        )
        return response.get("players_online", 0)

    async def servers_list(self, timeout: Optional[int] = None) -> List[Server]:
        """List all running servers and players that are online on them.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "onlinePlayers",
            timeout = timeout
        )

        del response["request"]

        # api sometimes returns such server, i guess just bug
        # "": []
        if "" in response:
            del response[""]

        return [Server(self._corkus, name, players) for name, players in response.items()]
