from corkus.utils.constants import URL_V1
from corkus.objects import OnlinePlayersSum
from corkus.objects.metadata import CorkusMetadata, APIVersion, EndpointKind


class NetworkEndpoint():
    def __init__(self, corkus) -> None:
        self.corkus = corkus

    async def online_players_sum(self) -> OnlinePlayersSum:
        response = await self.corkus.request.get(URL_V1 + "onlinePlayersSum")
        return OnlinePlayersSum(
            attributes = response,
            metadata = CorkusMetadata(
                version = APIVersion.V1,
                version_string = response["request"]["version"],
                kind = EndpointKind.ONLINE_PLAYERS_SUM
            )
        )
