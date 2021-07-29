from enum import Enum, IntEnum

class APIVersion(IntEnum):
    V1 = 1
    V2 = 2

class EndpointKind(Enum):
    TERITORY_LIST = "territoryList"
    ONLINE_PLAYERS_SUM = "onlinePlayersSum"

class CorkusMetadata:
    def __init__(
        self,
        version: APIVersion,
        version_string: str,
        kind: EndpointKind
    ):
        self.version = version
        self.version_string = version_string
        self.kind = kind
