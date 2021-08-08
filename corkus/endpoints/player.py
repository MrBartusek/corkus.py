from __future__ import annotations
from typing import TYPE_CHECKING, List

from corkus.endpoints.endpoint import Endpoint
from typing import Union
from corkus.utils.constants import URL_V2
from corkus.objects import Player, CorkusUUID

if TYPE_CHECKING:
    from corkus.objects import PartialPlayer

class PlayerEndpoint(Endpoint):
    async def get(self, username_or_uuid: Union[str, CorkusUUID]) -> Player:
        """Get statistics of specific player"""
        if isinstance(username_or_uuid, CorkusUUID):
            username_or_uuid = username_or_uuid.string(dashed = True)
        response = await self._corkus.request.get(URL_V2 + "player/" + username_or_uuid + "/stats")
        return Player(self._corkus, response)

    async def get_uuid(self, username: str) -> CorkusUUID:
        """Get UUID from player username

        This should not be used in place of the Mojang API, and your IP will be blocked if you do so"""
        response = await self._corkus.request.get(URL_V2 + "player/" + username + "/uuid")
        return CorkusUUID(response.get("uuid", ""))

    async def search(self, term: str) -> List[PartialPlayer]:
        """Search for players using specified search term"""
        result = await self._corkus.search.guilds_and_players(term)
        return result.players
