from __future__ import annotations
from typing import List, Coroutine, Any
from corkus.utils.constants import URL_V1
from corkus.endpoints.endpoint import Endpoint
from corkus.objects import Teritory

class TerritoryEndpoint(Endpoint):
    async def list_all(self) -> Coroutine[Any, Any, List[Teritory]]:
        """Get list of all possible teritories"""
        response = await self._corkus._request.get(URL_V1 + "territoryList")
        return [Teritory(self._corkus, t) for t in response.get("territories", {}).values()]
