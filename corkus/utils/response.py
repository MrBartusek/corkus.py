from aiohttp.client import ClientResponse
from enum import IntEnum, Enum

class APIVersion(IntEnum):
    V1 = 1
    V2 = 2

class EndpointKind(Enum):
    TERITORY_LIST = "territoryList"
    ONLINE_PLAYERS_SUM = "onlinePlayersSum"


class CorkusResponse:
    def __init__(
        self, *,
        version: APIVersion,
        version_string: str,
        kind: EndpointKind,
        raw_response: ClientResponse
    ):
        self.version = version
        self.version_string = version_string
        self.kind = kind
        self.raw_response = raw_response
