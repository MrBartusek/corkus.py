from corkus.utils.constants import URL_V1
from corkus.base import CorkusBase
from corkus.metadata import CorkusMetadata, APIVersion, EndpointKind

class OnlinePlayerSum(CorkusBase):
    @property
    def players_sum(self):
        return self.attributes.get("name", 0)

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
