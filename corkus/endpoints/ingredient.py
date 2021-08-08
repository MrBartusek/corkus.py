from __future__ import annotations
from typing import List, Coroutine, Any

from corkus.endpoints.endpoint import Endpoint
from corkus.utils.constants import URL_V2
from corkus.objects import Ingredient, PartialIngredient

class IngredientEndpoint(Endpoint):
    async def list_all(self) -> Coroutine[Any, Any, List[PartialIngredient]]:
        """List all available ingredient"""
        response = await self._corkus._request.get(URL_V2 + "ingredient/list")
        return [PartialIngredient(self._corkus, i) for i in response]

    async def get(self, name: str) -> Coroutine[Any, Any, Ingredient]:
        """Get information about ingredient of specified name"""
        response = await self._corkus._request.get(URL_V2 + "ingredient/get/" + name.replace(" ", "_"))
        return Ingredient(self._corkus, response)
