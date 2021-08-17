from __future__ import annotations
from typing import Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import SearchResult

class SearchEndpoint(Endpoint):
    async def guilds_and_players(self, term: str, timeout: Optional[int] = None) -> SearchResult:
        """Search for players and guilds in one requests.

        :param username: Search term.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "statsSearch&search=" + term,
            timeout = timeout
        )
        return SearchResult(self._corkus, response)
