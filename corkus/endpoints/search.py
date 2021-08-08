from __future__ import annotations
from typing import Coroutine, Any
from corkus.objects.search_result import SearchResult
from corkus.utils.constants import URL_V1
from corkus.endpoints.endpoint import Endpoint

class SearchEndpoint(Endpoint):
    async def guilds_and_players(self, term: str) -> Coroutine[Any, Any, SearchResult]:
        """Search for players and guilds in one requests"""
        response = await self._corkus._request.get(URL_V1 + "statsSearch&search=" + term)
        return SearchResult(self._corkus, response)
