from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import Recipe, PartialRecipe, ItemType, ProfessionType

class RecipeEndpoint(Endpoint):
    async def list_all(self, timeout: Optional[int] = None) -> List[PartialRecipe]:
        """List all available recipe.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/list",
            timeout = timeout
        )
        return [PartialRecipe(self._corkus, r) for r in response.get("data", [])]

    async def get(self) -> Recipe:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def get_by_id(self, recipe_id: str, timeout: Optional[int] = None) -> Recipe:
        """Get information about recipe by id like ``Food-13-15`` or ``Wand-63-65``.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/get/" + recipe_id,
            timeout = timeout
        )
        return Recipe(self._corkus, response.get("data", {})[0])

    async def search_by_type(self, type: ItemType, timeout: Optional[int] = None) -> List[Recipe]:
        """Search for the ingredients using type
        (:py:attr:`Recipe.type <corkus.objects.Recipe.type>`).

        :param name: Type of returned recipes.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/search/type/" + type.value.lower(),
            timeout = timeout
        )
        return [Recipe(self._corkus, r) for r in response.get("data", [])]

    async def search_by_profession(self, profession: ProfessionType, timeout: Optional[int] = None) -> List[Recipe]:
        """Search for the ingredients using profession
        (:py:attr:`Recipe.profession <corkus.objects.Recipe.profession>`).

        :param profession: Required profession for returned recipes.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/search/skill/" + profession.value.lower(),
            timeout = timeout
        )
        return [Recipe(self._corkus, r) for r in response.get("data", [])]

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
