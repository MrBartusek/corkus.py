
from typing import List
from corkus.utils.constants import URL_V1
from corkus.objects import LeaderboardPlayer, LeaderboardGuild
from corkus.endpoints.endpoint import Endpoint

class LeaderboardEndpoint(Endpoint):
    async def guild(self) -> List[LeaderboardGuild]:
        """Returns a leaderboard of guilds with a length of 100. Sorted by territories currently owned, then level"""
        response = await self.corkus.request.get(URL_V1 + "statsLeaderboard&type=guild&timeframe=alltime")
        return [LeaderboardGuild(self.corkus, g) for g in response]

    async def combat(self) -> List[LeaderboardPlayer]:
        """Returns a leaderboard of players with a length of 100. Sorted by player combat level/xp"""
        response = await self.corkus.request.get(URL_V1 + "statsLeaderboard&type=player&timeframe=alltime")
        return [LeaderboardPlayer(self.corkus, g) for g in response]

    async def pvp(self) -> List[LeaderboardPlayer]:
        """Returns a leaderboard of players with a length of 100. Sorted by PvP kills"""
        response = await self.corkus.request.get(URL_V1 + "statsLeaderboard&type=pvp&timeframe=alltime")
        return [LeaderboardPlayer(self.corkus, g) for g in response]
