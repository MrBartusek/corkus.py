
from corkus.objects.search_result import SearchResult
from corkus.utils.constants import URL_V1
from corkus.endpoints.endpoint import Endpoint

class SearchEndpoint(Endpoint):
    async def guilds_and_players(self, term: str) -> SearchResult:
        """Search for players and guilds in one requests"""
        response = await self.corkus.request.get(URL_V1 + "statsSearch&search=" + term)
        return SearchResult(self.corkus, response)
