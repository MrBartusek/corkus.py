from typing import List

from corkus.endpoints.endpoint import Endpoint
from corkus.utils.constants import URL_V2
from corkus.objects import Recipe, PartialRecipe

class RecipeEndpoint(Endpoint):
    async def list_all(self) -> List[PartialRecipe]:
        """List all available recipe"""
        response = await self._corkus._request.get(URL_V2 + "recipe/list")
        return [PartialRecipe(self._corkus, r) for r in response]

    async def get_by_id(self, recipe_id: str) -> Recipe:
        """Get information about recipe by id like `Food-13-15` or `Wand-63-65`"""
        response = await self._corkus._request.get(URL_V2 + "recipe/get/" + recipe_id)
        return Recipe(self._corkus, response)
