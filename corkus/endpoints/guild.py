from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import PartialGuild, Guild

class GuildEndpoint(Endpoint):
    async def list_all(self, timeout: Optional[int] = None) -> List[PartialGuild]:
        """List all active guild on the server.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "guildList",
            timeout = timeout
        )
        return [PartialGuild(self._corkus, g) for g in response.get("guilds", [])]

    async def get(self, name: str, timeout: Optional[int] = None) -> Guild:
        """Get statics of the guild by given name.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "guildStats&command=" + name,
            timeout = timeout
        )
        return Guild(self._corkus, response)

    async def search(self, term: str, timeout: Optional[int] = None) -> List[PartialGuild]:
        """Search for guilds using specified search term.

        :param term: Search term for guild search.
        :param timeout: Optionally override default timeout.
        """
        result = await self._corkus.search.guilds_and_players(term, timeout)
        return result.guilds
