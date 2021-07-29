from corkus.utils.constants import URL_V1

class NetworkEndpoint():
    def __init__(self, corkus) -> None:
        self.corkus = corkus

    async def players_sum(self) -> int:
        response = await self.corkus.request.get(URL_V1 + "onlinePlayersSum")
        return response.get("players_online", 0)

    async def servers_list(self) -> None:
        pass
