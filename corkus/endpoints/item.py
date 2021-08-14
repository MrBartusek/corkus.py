
from corkus.errors import InvalidInputError
from typing import List
from corkus.utils.constants import URL_V1
from corkus.objects import Item, ItemType
from corkus.endpoints.endpoint import Endpoint

class ItemEndpoint(Endpoint):
    async def get_all(self) -> List[Item]:
        """List all available items.

        .. include:: ../note_big_endpoint.rst"""
        response = await self._corkus.request.get(URL_V1 + "itemDB&category=all")
        return [Item(self._corkus, i) for i in response.get("items", {})]

    async def search_by_type(self, type: ItemType) -> List[Item]:
        """Search for the items using their type
        (:py:attr:`Item.type <corkus.objects.Item.type>`).

        .. py:currentmodule:: corkus.objects

        .. warning::
            This function does not accept crafted items:
            :py:attr:`ItemType.SCROLL`, :py:attr:`ItemType.POTION` and
            :py:attr:`ItemType.FOOD`. Providing them will raise
            :py:exc:`corkus.errors.InvalidInputError`

        :param type: The type of returned items.
        :raises InvalidInputError: When invalid type is provided."""
        if type in (ItemType.SCROLL, ItemType.FOOD, ItemType.POTION):
            raise InvalidInputError(f"Searching for crafteds items, like {type}, is not possible.")

        response = await self._corkus.request.get(URL_V1 + "itemDB&category=" + type.value.lower())
        return [Item(self._corkus, i) for i in response.get("items", {})]

    async def search_by_name(self, name: str) -> List[Item]:
        """Search for the items using their name
        (:py:attr:`Item.name <corkus.objects.Item.name>`).

        :param name: The name of returned items."""
        response = await self._corkus.request.get(URL_V1 + "itemDB&search=" + name)
        return [Item(self._corkus, i) for i in response.get("items", {})]
