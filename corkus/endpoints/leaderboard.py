from __future__ import annotations
from typing import List, Optional

from .endpoint import Endpoint
from corkus.utils.request import APIVersion
from corkus.objects import LeaderboardPlayer, LeaderboardGuild, Timeframe

class LeaderboardEndpoint(Endpoint):
    async def guild(self, timeout: Optional[int] = None) -> List[LeaderboardGuild]:
        """Returns a leaderboard of guilds with a length of 100. Sorted by territories
        currently owned, then level.

        :param timeout: Optionally override default timeout."""
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "statsLeaderboard&type=guild&timeframe=alltime",
            timeout = timeout
        )
        return [LeaderboardGuild(self._corkus, g) for g in response.get("data", [])]

    async def combat(self, timeout: Optional[int] = None) -> List[LeaderboardPlayer]:
        """Returns a leaderboard of players with a length of 100. Sorted by player combat level/xp.

        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "statsLeaderboard&type=player&timeframe=alltime",
            timeout = timeout
        )
        return [LeaderboardPlayer(self._corkus, g) for g in response.get("data", [])]

    async def pvp(self, *, timeframe: Optional[Timeframe] = Timeframe.ALL_TIME, timeout: Optional[int] = None) -> List[LeaderboardPlayer]:
        """Returns a leaderboard of players with a length of 100. Sorted by
        :py:attr:`LeaderboardPlayer.pvp_kills <corkus.objects.LeaderboardPlayer.pvp_kills>`.

        .. caution::
            Since `The Nether <https://wynncraft.fandom.com/wiki/The_Nether>`_ is disabled
            changing ``timeframe`` doesn't do anything.

        :param timeframe: Timeframe for results will be returned.
        :param timeout: Optionally override default timeout.
        """
        response = await self._request.get(
            version = APIVersion.V1,
            parameters = "statsLeaderboard&type=pvp&timeframe=" + timeframe.value,
            timeout = timeout
        )
        return [LeaderboardPlayer(self._corkus, g) for g in response.get("data", [])]
