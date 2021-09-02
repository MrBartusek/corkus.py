from __future__ import annotations
from corkus.objects.identification_type import IdentificationType
from typing import List, Literal, Optional, Tuple, Union

from ..utils.utils import Utils
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
            parameters = "ingredient/search/tier/" + str(tier),
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
            parameters = "ingredient/search/level/" + str(level),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_professions(self, symbol: LogicSymbol, professions: List[ProfessionType], timeout: Optional[int] = None) -> List[Ingredient]:
        """.. include:: moderate_route.rst

        Search for the ingredients using their required professions
        (:py:attr:`Ingredient.required_professions <corkus.objects.Ingredient.required_professions>`).

        :param symbol: Logic symbol to be used on ingredients list.
        :param professions: List of professions to search for.
        :param timeout: Optionally override default timeout.
        """
        professions = [s.value.lower() for s in professions]

        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/skills/" + symbol.value + ",".join(professions),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_sprite(self,
        symbol: LogicSymbol, *,
        id: Optional[int],
        damage: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Ingredient]:
        """.. include:: complex_route.rst

        Search for the ingredients using properties in
        :py:attr:`Ingredient.sprite <corkus.objects.Ingredient.sprite>`.

        :param symbol: Logic symbol to be used on this query.
        :param id: Ingredient property.
        :param damage: Ingredient property.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/sprite/" + Utils.build_complex_query(symbol, id = id, damage = damage),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_identifications(self,
        symbol: LogicSymbol,
        identifications: List[Tuple[IdentificationType, Union[int, None], Union[int, None]]],
        timeout: Optional[int] = None
    ) -> List[Ingredient]:
        """.. include:: complex_route.rst

        Search for the ingredients using values of their identifications
        :py:attr:`Ingredient.identifications <corkus.objects.Ingredient.identifications>`.

        Example:

        .. code-block:: python

            # Search for ingredient that have xp bonus between 4 and 6 AND any loot bonus

            await corkus.ingredient.search_by_identifications(
                LogicSymbol.AND,
                [
                    (IdentificationType.XP_BONUS, 4, 6),
                    (IdentificationType.LOOT_BONUS, None, None),
                ]
            )

        :param symbol: Logic symbol to be used on this query.
        :param identifications:
            List of tuples with exactly three elements.

            * Type of the identification.

            * If a :py:class:`int`, the :py:attr:`min <corkus.objects.IdentificationValues.min>`
              for such identification must have that value. If :py:class:`None`, the
              :py:attr:`min <corkus.objects.IdentificationValues.min>` for such identification
              can be anything.

            * If a :py:class:`int`, the :py:attr:`max <corkus.objects.IdentificationValues.max>`
              for such identification must have that value. If :py:class:`None`, the
              :py:attr:`max <corkus.objects.IdentificationValues.max>` for such identification
              can be anything.

        :param timeout: Optionally override default timeout.
        """
        query = {}
        for i in identifications:
            query[IdentificationType.to_ingredient_api(i[0])] = (
                str(i[1] if i[1] is not None else "") + ";" + str(i[2] if i[2] is not None else "")
            )

        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/identifications/" + Utils.build_complex_query(symbol, **query),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_item_modifiers(self,
        symbol: LogicSymbol, *,
        durability: Optional[int] = None,
        strength: Optional[int] = None,
        dexterity: Optional[int] = None,
        intelligence: Optional[int] = None,
        defence: Optional[int] = None,
        agility: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Ingredient]:
        """.. include:: complex_route.rst

        Search for the ingredients using properties in
        :py:attr:`Ingredient.item_modifiers <corkus.objects.Ingredient.item_modifiers>`.

        :param symbol: Logic symbol to be used on this query.
        :param durability: Ingredient property.
        :param strength: Ingredient property.
        :param dexterity: Ingredient property.
        :param intelligence: Ingredient property.
        :param defence: Ingredient property.
        :param agility: Ingredient property.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/itemOnlyIDs/" + Utils.build_complex_query(
                symbol,
                durability = durability,
                strength = strength,
                dexterity = dexterity,
                intelligence = intelligence,
                defence = defence,
                agility = agility
            ),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]

    async def search_by_consumable_modifiers(self,
        symbol: LogicSymbol, *,
        duration: Optional[int] = None,
        charges: Optional[int] = None,
        timeout: Optional[int] = None
    ) -> List[Ingredient]:
        """.. include:: complex_route.rst

        Search for the ingredients using properties in
        :py:attr:`Ingredient.consumable_modifiers <corkus.objects.Ingredient.consumable_modifiers>`.

        :param symbol: Logic symbol to be used on this query.
        :param duration: Ingredient property.
        :param charges: Ingredient property.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V2,
            parameters = "ingredient/search/consumableOnlyIDs/" + Utils.build_complex_query(
                symbol,
                duration = duration,
                charges = charges
            ),
            timeout = timeout
        )
        return [Ingredient(self._corkus, i) for i in response.get("data", [])]
