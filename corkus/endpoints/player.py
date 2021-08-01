from corkus.endpoints.endpoint import Endpoint
from typing import Union
from corkus.utils.constants import URL_V2
from corkus.objects import Player, CorkusUUID

class PlayerEndpoint(Endpoint):
    async def get(self, username_or_uuid: Union[str, CorkusUUID]) -> Player:
        """Get statistics of specific player"""
        if isinstance(username_or_uuid, CorkusUUID):
            username_or_uuid = username_or_uuid.string(dashed = True)
        response = await self.corkus.request.get(URL_V2 + "player/" + username_or_uuid + "/stats")
        return Player(self.corkus, response)

    async def get_uuid(self, username: str) -> CorkusUUID:
        """Get UUID from player username

        This should not be used in place of the Mojang API, and your IP will be blocked if you do so
        """
        response = await self.corkus.request.get(URL_V2 + "player/" + username + "/uuid")
        return CorkusUUID(response["uuid"])
