from typing import List

from corkus.endpoints.endpoint import Endpoint
from corkus.utils.constants import URL_V2
from corkus.objects import Recipe, PartialRecipe, ItemType, ProfessionType

class RecipeEndpoint(Endpoint):
    async def list_all(self) -> List[PartialRecipe]:
        """List all available recipe"""
        response = await self._corkus.request.get(URL_V2 + "recipe/list")
        return [PartialRecipe(self._corkus, r) for r in response]

    async def get(self) -> Recipe:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def get_by_id(self, recipe_id: str) -> Recipe:
        """Get information about recipe by id like ``Food-13-15`` or ``Wand-63-65``"""
        response = await self._corkus.request.get(URL_V2 + "recipe/get/" + recipe_id)
        return Recipe(self._corkus, response)

    async def search_by_type(self, type: ItemType) -> List[Recipe]:
        """Search for the ingredients using type
        (:py:attr:`Recipe.type <corkus.objects.Recipe.type>`).

        :param name: Type of returned recipes."""
        response = await self._corkus.request.get(URL_V2 + "recipe/search/type/" + type.value.capitalize())
        return [Recipe(self._corkus, r) for r in response]

    async def search_by_profession(self, profession: ProfessionType) -> List[Recipe]:
        """Search for the ingredients using profession
        (:py:attr:`Recipe.profession <corkus.objects.Recipe.profession>`).

        :param profession: Required profession for returned recipes."""
        response = await self._corkus.request.get(URL_V2 + "recipe/search/skill/" + profession.value.capitalize())
        return [Recipe(self._corkus, r) for r in response]

    async def search_by_level(self) -> List[Recipe]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def search_by_duration(self) -> List[Recipe]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def search_by_health_or_damage(self) -> List[Recipe]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def search_by_durability(self) -> List[Recipe]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError
