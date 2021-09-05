from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Union

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import Player, CorkusUUID

if TYPE_CHECKING:
    from corkus.objects import PartialPlayer

class PlayerEndpoint(Endpoint):
    async def get(self, username_or_uuid: Union[str, CorkusUUID], timeout: Optional[int] = None) -> Player:
        """Get statistics of specific player.

        .. note::
            If you are getting player by UUID please make sure it's in
            the dashed form or, even better, wrap it intro :py:class:`CorkusUUID <corkus.objects.CorkusUUID>`
            like so:

            .. code-block:: python

                corkus.player.get(CorkusUUID(uuid))

        :param username_or_uuid: Username or UUID of the player.
        :param timeout: Optionally override default timeout.
        """
        if isinstance(username_or_uuid, CorkusUUID):
            username_or_uuid = username_or_uuid.string(dashed = True)

        response = await self._request.get(
            version = APIVersion.V2,
            parameters = f"player/{username_or_uuid}/stats",
            timeout = timeout
        )
        return Player(self._corkus, response.get("data", {})[0])

    async def get_uuid(self, username: str, timeout: Optional[int] = None) -> CorkusUUID:
        """Get UUID from player username

        .. danger::
            This should not be used in place of the Mojang API, and your IP will be blocked if you do so.

        :param username: Username of the player.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = f"player/{username}/uuid",
            timeout = timeout
        )
        return CorkusUUID(response.get("data", [])[0].get("uuid", ""))

    async def search(self, term: str, timeout: Optional[int] = None) -> List[PartialPlayer]:
        """Search for players using specified search term.

        :param username: Search term.
        :param timeout: Optionally override default timeout.
        """
        result = await self._corkus.search.guilds_and_players(term, timeout)
        return result.players
