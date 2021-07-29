from corkus.utils.constants import URL_V1
from corkus.objects import OnlinePlayersSum

class NetworkEndpoint():
    def __init__(self, corkus) -> None:
        self.corkus = corkus

    async def online_players_sum(self) -> OnlinePlayersSum:
        response = await self.corkus.request.get(URL_V1 + "onlinePlayersSum")
        return OnlinePlayersSum(response)
