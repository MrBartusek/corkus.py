from corkus.utils.constants import URL_V1
from corkus.utils.response import CorkusResponse, APIVersion, EndpointKind
from typing import Awaitable

class OnlinePlayerSumResponse(CorkusResponse):
    def __init__(self, response):
        super().__init__(
            version = APIVersion.V1,
            version_string = response["request"]["version"],
            kind = EndpointKind.ONLINE_PLAYERS_SUM,
            raw_response = response
        )
        self.online_players_sum: int = response["players_online"]

class Network():
    def __init__(self, corkus) -> None:
        self.corkus = corkus

    async def online_players_sum(self) -> OnlinePlayerSumResponse:
        response = await self.corkus.request.get(URL_V1 + "onlinePlayersSum")
        return OnlinePlayerSumResponse(response)

        