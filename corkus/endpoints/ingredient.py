from typing import List

from corkus.endpoints.endpoint import Endpoint
from corkus.utils.constants import URL_V2
from corkus.objects import Ingredient, PartialIngredient

class IngredientEndpoint(Endpoint):
    async def list_all(self) -> List[PartialIngredient]:
        """List all available ingredient"""
        response = await self._corkus.request.get(URL_V2 + "ingredient/list")
        return [PartialIngredient(self._corkus, i) for i in response]

    async def get(self, name: str) -> Ingredient:
        """Get information about ingredient of specified name"""
        response = await self._corkus.request.get(URL_V2 + "ingredient/get/" + name.replace(" ", "_"))
        return Ingredient(self._corkus, response)
