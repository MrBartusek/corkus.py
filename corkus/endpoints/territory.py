
from typing import List
from corkus.utils.constants import URL_V1
from corkus.endpoints.endpoint import Endpoint
from corkus.objects import Territory

class TerritoryEndpoint(Endpoint):
    async def list_all(self) -> List[Territory]:
        """Get list of all possible teritories"""
        response = await self._corkus.request.get(URL_V1 + "territoryList")
        return [Territory(self._corkus, t) for t in response.get("territories", {}).values()]
