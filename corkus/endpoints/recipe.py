from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import Recipe, PartialRecipe, ItemType, ProfessionType, LogicSymbol
from corkus.utils.utils import Utils

class RecipeEndpoint(Endpoint):
    async def list_all(self, timeout: Optional[int] = None) -> List[PartialRecipe]:
        """List all available recipes.

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

    async def search_by_level(self,
        symbol: LogicSymbol, *,
        min: Optional[int] = None,
        max: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Recipe]:
        """.. include:: complex_route.rst

        Search for the recipes using their
        :py:attr:`Recipe.level <corkus.objects.Recipe.level>`.

        :param symbol: Logic symbol to be used on this query.
        :param min: Minimum level.
        :param max: Maximum level.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/search/level/" + Utils.build_complex_query(symbol, minimum = min, maximum = max),
            timeout = timeout
        )
        return [Recipe(self._corkus, i) for i in response.get("data", [])]

    async def search_by_durability(self,
        symbol: LogicSymbol, *,
        min: Optional[int] = None,
        max: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Recipe]:
        """.. include:: complex_route.rst

        Search for the recipes using their
        :py:attr:`Recipe.durability <corkus.objects.Recipe.durability>`.

        :param symbol: Logic symbol to be used on this query.
        :param min: Minimum durability identification.
        :param max: Maximum durability identification.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/search/durability/" + Utils.build_complex_query(symbol, minimum = min, maximum = max),
            timeout = timeout
        )
        return [Recipe(self._corkus, i) for i in response.get("data", [])]

    async def search_by_health_or_damage(self,
        symbol: LogicSymbol, *,
        min: Optional[int] = None,
        max: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Recipe]:
        """.. include:: complex_route.rst

        Search for the recipes using their
        :py:attr:`Recipe.health_or_damage <corkus.objects.Recipe.health_or_damage>`.

        :param symbol: Logic symbol to be used on this query.
        :param min: Minimum *health or damage* identification.
        :param max: Maximum *health or damage* identification.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/search/healthOrDamage/" + Utils.build_complex_query(symbol, minimum = min, maximum = max),
            timeout = timeout
        )
        return [Recipe(self._corkus, i) for i in response.get("data", [])]

    async def search_by_duration(self,
        symbol: LogicSymbol, *,
        min: Optional[int] = None,
        max: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Recipe]:
        """.. include:: complex_route.rst

        Search for the recipes using their
        :py:attr:`Recipe.duration <corkus.objects.Recipe.duration>`.

        :param symbol: Logic symbol to be used on this query.
        :param min: Minimum duration identification.
        :param max: Maximum duration identification.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "recipe/search/duration/" + Utils.build_complex_query(symbol, minimum = min, maximum = max),
            timeout = timeout
        )
        return [Recipe(self._corkus, i) for i in response.get("data", [])]
