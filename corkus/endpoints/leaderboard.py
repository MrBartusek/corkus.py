
from typing import List, Optional
from corkus.utils.constants import URL_V1
from corkus.objects import LeaderboardPlayer, LeaderboardGuild, Timeframe
from corkus.endpoints.endpoint import Endpoint

class LeaderboardEndpoint(Endpoint):
    async def guild(self) -> List[LeaderboardGuild]:
        """Returns a leaderboard of guilds with a length of 100. Sorted by territories currently owned, then level"""
        response = await self._corkus.request.get(URL_V1 + "statsLeaderboard&type=guild&timeframe=alltime")
        return [LeaderboardGuild(self._corkus, g) for g in response]

    async def combat(self) -> List[LeaderboardPlayer]:
        """Returns a leaderboard of players with a length of 100. Sorted by player combat level/xp"""
        response = await self._corkus.request.get(URL_V1 + "statsLeaderboard&type=player&timeframe=alltime")
        return [LeaderboardPlayer(self._corkus, g) for g in response]

    async def pvp(self, timeframe: Optional[Timeframe] = Timeframe.ALL_TIME) -> List[LeaderboardPlayer]:
        """Returns a leaderboard of players with a length of 100. Sorted by
        :py:attr:`LeaderboardPlayer.pvp_kills <corkus.objects.LeaderboardPlayer.pvp_kills>`.

        :param timeframe: Timeframe for results will be returned.

            .. caution::
                Since `The Nether <https://wynncraft.fandom.com/wiki/The_Nether>`_ is disabled
                changing ``timeframe`` doesn't do anything."""
        response = await self._corkus.request.get(URL_V1 + "statsLeaderboard&type=pvp&timeframe=" + timeframe.value)
        return [LeaderboardPlayer(self._corkus, g) for g in response]
