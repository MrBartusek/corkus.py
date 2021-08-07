from typing import List
from corkus.utils.constants import URL_V1
from corkus.objects import Server
from corkus.endpoints.endpoint import Endpoint

class NetworkEndpoint(Endpoint):
    async def players_sum(self) -> int:
        """Get number of online players across all servers"""
        response = await self._corkus._request.get(URL_V1 + "onlinePlayersSum")
        return response.get("players_online", 0)

    async def servers_list(self) -> List[Server]:
        """List all running servers and players that are online on them"""
        response = await self._corkus._request.get(URL_V1 + "onlinePlayers")
        del response["request"]

        # api sometimes returns such server, i guess just bug
        # "": []
        if "" in response:
            del response[""]

        return [Server(self._corkus, name, players) for name, players in response.items()]
