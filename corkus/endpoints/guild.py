
from typing import List
from corkus.utils.constants import URL_V1
from corkus.objects import PartialGuild, Guild
from corkus.endpoints.endpoint import Endpoint

class GuildEndpoint(Endpoint):
    async def list_all(self) -> List[PartialGuild]:
        """List all active guild on the server"""
        response = await self.corkus.request.get(URL_V1 + "guildList")
        return [PartialGuild(self.corkus, g) for g in response.get("guilds", [])]

    async def get(self, name: str) -> Guild:
        """Get statics of the guild by given name"""
        response = await self.corkus.request.get(URL_V1 + "guildStats&command=" + name)
        return Guild(self.corkus, response)

    async def search(self, term: str) -> List[PartialGuild]:
        """Search for guilds using specified search term"""
        result = await self.corkus.search.guilds_and_players(term)
        return result.guilds
