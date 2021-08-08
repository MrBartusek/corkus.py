from __future__ import annotations
from typing import List, Coroutine, Any
from corkus.utils.constants import URL_V1
from corkus.objects import PartialGuild, Guild
from corkus.endpoints.endpoint import Endpoint

class GuildEndpoint(Endpoint):
    async def list_all(self) -> Coroutine[Any, Any, List[PartialGuild]]:
        """List all active guild on the server"""
        response = await self._corkus._request.get(URL_V1 + "guildList")
        return [PartialGuild(self._corkus, g) for g in response.get("guilds", [])]

    async def get(self, name: str) -> Coroutine[Any, Any, Guild]:
        """Get statics of the guild by given name"""
        response = await self._corkus._request.get(URL_V1 + "guildStats&command=" + name)
        return Guild(self._corkus, response)

    async def search(self, term: str) -> Coroutine[Any, Any, List[PartialGuild]]:
        """Search for guilds using specified search term"""
        result = await self._corkus.search.guilds_and_players(term)
        return result.guilds
