from __future__ import annotations
from typing import List, Literal, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import Ingredient, PartialIngredient, LogicSymbol, ProfessionType

class IngredientEndpoint(Endpoint):
    async def list_all(self, timeout: Optional[int] = None) -> List[PartialIngredient]:
        """List all available ingredient.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/list",
            timeout = timeout
        )
        return [PartialIngredient(self._corkus, i) for i in response.get("data", [])]

    async def get(self, name: str, timeout: Optional[int] = None) -> Ingredient:
        """Get information about ingredient of specified name

        :param name: the name of the ingredient
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/get/" + name.replace(" ", "_"),
            timeout = timeout
        )
        return Ingredient(self._corkus, response.get("data", {})[0])

    async def search_by_name(self, name: str, timeout: Optional[int] = None) -> List[Ingredient]:
        """Search for the ingredients using name
        (:py:attr:`Ingredient.name <corkus.objects.Ingredient.name>`).
        For geting ingredient by specified name see: :py:func:`get`.

        :param name: Search term.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/name/" + name,
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_tier(self, tier: Literal[0, 1, 2, 3], timeout: Optional[int] = None) -> List[Ingredient]:
        """Search for the ingredients using their tier
        (:py:attr:`Ingredient.tier <corkus.objects.Ingredient.tier>`).

        :param tier: Tier of returned ingredients.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/tier/" + tier,
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_level(self, level: int, timeout: Optional[int] = None) -> List[Ingredient]:
        """Search for the ingredients using their level
        (:py:attr:`Ingredient.required_level <corkus.objects.Ingredient.required_level>`).

        :param level: Level of returned ingredients.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/level/" + level,
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_professions(self, symbol: LogicSymbol, professions: List[ProfessionType], timeout: Optional[int] = None) -> List[Ingredient]:
        """Search for the ingredients using their required professions
        (:py:attr:`Ingredient.required_professions <corkus.objects.Ingredient.required_professions>`).

        :param symbol: Logic symbol to be used on ingredients list.
        :param professions: List of professions to search for.
        :param timeout: Optionally override default timeout.
        """
        professions = [s.value.lower() for s in professions]

        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/skills/" + symbol + professions.join(","),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_sprite(self) -> List[Ingredient]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def search_by_identifications(self) -> List[Ingredient]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def search_by_item_modifiers(self) -> List[Ingredient]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError

    async def search_by_consumable_modifiers(self) -> List[Ingredient]:
        """.. include:: ../note_not_implemented.rst"""
        raise NotImplementedError
