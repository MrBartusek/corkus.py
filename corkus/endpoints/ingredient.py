from typing import List, Literal

from corkus.endpoints.endpoint import Endpoint
from corkus.utils.constants import URL_V2
from corkus.objects import Ingredient, PartialIngredient, LogicSymbol, ProfessionType

class IngredientEndpoint(Endpoint):
    async def list_all(self) -> List[PartialIngredient]:
        """List all available ingredient"""
        response = await self._corkus.request.get(URL_V2 + "ingredient/list")
        return [PartialIngredient(self._corkus, i) for i in response]

    async def get(self, name: str) -> Ingredient:
        """Get information about ingredient of specified name

        :param name: the name of the ingredient"""
        response = await self._corkus.request.get(URL_V2 + "ingredient/get/" + name.replace(" ", "_"))
        return Ingredient(self._corkus, response)

    async def search_by_name(self, name: str) -> List[Ingredient]:
        """Search for the ingredients using name
        (:py:attr:`Ingredient.name <corkus.objects.Ingredient.name>`).
        For geting ingredient by specified name see: :py:func:`get`.

        :param name: search term"""
        response = await self._corkus.request.get(URL_V2 + "ingredient/search/name/" + name)
        return [Ingredient(self._corkus, i) for i in response]

    async def search_by_tier(self, tier: Literal[0, 1, 2, 3]) -> List[Ingredient]:
        """Search for the ingredients using their tier
        (:py:attr:`Ingredient.tier <corkus.objects.Ingredient.tier>`).

        :param tier: tier of returned ingredients."""
        response = await self._corkus.request.get(URL_V2 + "ingredient/search/tier/" + tier)
        return [Ingredient(self._corkus, i) for i in response]

    async def search_by_level(self, level: int) -> List[Ingredient]:
        """Search for the ingredients using their level
        (:py:attr:`Ingredient.required_level <corkus.objects.Ingredient.required_level>`).

        :param level: level of returned ingredients."""
        response = await self._corkus.request.get(URL_V2 + "ingredient/search/level/" + level)
        return [Ingredient(self._corkus, i) for i in response]

    async def search_by_professions(self, symbol: LogicSymbol, professions: List[ProfessionType]) -> List[Ingredient]:
        """Search for the ingredients using their required professions
        (:py:attr:`Ingredient.required_professions <corkus.objects.Ingredient.required_professions>`).

        :param symbol: logic symbol to be used on ingredients list.
        :param professions: list of professions to search for."""
        professions = [s.value.lower() for s in professions]

        response = await self._corkus.request.get(URL_V2 + "ingredient/search/skills/" + symbol + professions.join(","))
        return [Ingredient(self._corkus, i) for i in response]

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
