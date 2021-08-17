from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import Territory

class TerritoryEndpoint(Endpoint):
    async def list_all(self, timeout: Optional[int] = None) -> List[Territory]:
        """Get list of all possible teritories.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "territoryList",
            timeout = timeout
        )
        return [Territory(self._corkus, t) for t in response.get("territories", {}).values()]
