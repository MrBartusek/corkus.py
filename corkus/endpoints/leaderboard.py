from __future__ import annotations
from typing import List, Optional, Coroutine, Any
from corkus.utils.constants import URL_V1
from corkus.objects import LeaderboardPlayer, LeaderboardGuild, Timeframe
from corkus.endpoints.endpoint import Endpoint

class LeaderboardEndpoint(Endpoint):
    async def guild(self) -> Coroutine[Any, Any, List[LeaderboardGuild]]:
        """Returns a leaderboard of guilds with a length of 100. Sorted by territories currently owned, then level"""
        response = await self._corkus._request.get(URL_V1 + "statsLeaderboard&type=guild&timeframe=alltime")
        return [LeaderboardGuild(self._corkus, g) for g in response]

    async def combat(self) -> Coroutine[Any, Any, List[LeaderboardPlayer]]:
        """Returns a leaderboard of players with a length of 100. Sorted by player combat level/xp"""
        response = await self._corkus._request.get(URL_V1 + "statsLeaderboard&type=player&timeframe=alltime")
        return [LeaderboardPlayer(self._corkus, g) for g in response]

    async def pvp(self, timeframe: Optional[Timeframe] = Timeframe.ALL_TIME) -> Coroutine[Any, Any, List[LeaderboardPlayer]]:
        """Returns a leaderboard of players with a length of 100. Sorted by PvP kills"""
        response = await self._corkus._request.get(URL_V1 + "statsLeaderboard&type=pvp&timeframe=" + timeframe.value)
        return [LeaderboardPlayer(self._corkus, g) for g in response]
