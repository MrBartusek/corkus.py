
from typing import List
from corkus.utils.constants import URL_V1
from corkus.endpoints.endpoint import Endpoint
from corkus.objects import Teritory

class TerritoryEndpoint(Endpoint):
    async def list_all(self) -> List[Teritory]:
        """Get list of all possible teritories"""
        response = await self.corkus.request.get(URL_V1 + "territoryList")
        return [Teritory(self.corkus, t) for t in response.get("territories", {}).values()]
