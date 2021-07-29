from corkus.utils.constants import URL_V1
from corkus.base import CorkusBase
from corkus.metadata import CorkusMetadata, APIVersion, EndpointKind

class OnlinePlayerSum(CorkusBase):
    @property
    def players_sum(self) -> int:
        return self.attributes.get("players_online", 0)

    def __int__(self) -> int:
        return self.players_sum

class NetworkEndpoint():
    def __init__(self, corkus) -> None:
        self.corkus = corkus

    async def online_players_sum(self) -> OnlinePlayerSum:
        response = await self.corkus.request.get(URL_V1 + "onlinePlayersSum")
        return OnlinePlayerSum(
            attributes = response,
            metadata = CorkusMetadata(
                version = APIVersion.V1,
                version_string = response["request"]["version"],
                kind = EndpointKind.ONLINE_PLAYERS_SUM
            )
        )
