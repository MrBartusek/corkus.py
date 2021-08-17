from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.errors import InvalidInputError
from corkus.objects import Item, ItemType

class ItemEndpoint(Endpoint):
    async def get_all(self, timeout: Optional[int] = None) -> List[Item]:
        """List all available items.

        .. include:: ../note_big_endpoint.rst

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "itemDB&category=all",
            timeout = timeout
        )
        return [Item(self._corkus, i) for i in response.get("items", [])]

    async def search_by_type(self, type: ItemType, timeout: Optional[int] = None) -> List[Item]:
        """Search for the items using their type
        (:py:attr:`Item.type <corkus.objects.Item.type>`).

        .. py:currentmodule:: corkus.objects

        .. warning::
            This function does not accept crafted items: :py:attr:`ItemType.SCROLL`,
            :py:attr:`ItemType.POTION` and :py:attr:`ItemType.FOOD`. Providing them
            will raise :py:exc:`corkus.errors.InvalidInputError`

        :param type: The type of returned items.
        :param timeout: Optionally override default timeout.
        :raises InvalidInputError: When invalid type is provided.
        """
        if type in (ItemType.SCROLL, ItemType.FOOD, ItemType.POTION):
            raise InvalidInputError(f"Searching for crafteds items, like {type}, is not possible.")

        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "itemDB&category=" + type.value.lower(),
            timeout = timeout
        )
        return [Item(self._corkus, i) for i in response.get("items", [])]

    async def search_by_name(self, name: str, timeout: Optional[int] = None) -> List[Item]:
        """Search for the items using their name
        (:py:attr:`Item.name <corkus.objects.Item.name>`).

        :param name: Search term.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "itemDB&search=" + name,
            timeout = timeout
        )
        return [Item(self._corkus, i) for i in response.get("items", [])]
