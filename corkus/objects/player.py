from __future__ import annotations
from corkus.objects.playtime import PlayerPlaytime
from typing import List, Union
import iso8601
import datetime
from deprecated.sphinx import deprecated

from .base_player import BasePlayer
from .partial_member import PartialMember
from .partial_guild import PartialGuild
from .member import GuildRank
from .player_status import PlayerStatus
from .player_statistics import PlayerStatistics
from .player_character import Character
from .dungeon import Dungeon
from .raid import Raid
from .quest import Quest
from .player_ranking import Ranking

class Player(BasePlayer):
    """Represents a player of a Wynncraft server."""
    @property
    def username(self) -> str:
        """Minecraft username of player."""
        return self._attributes.get("username", "")

    @property
    def join_date(self) -> datetime.datetime:
        """Date and time when player joined Wynncraft for the first time."""
        return iso8601.parse_date(self._attributes.get("meta", {}).get("firstJoin", "1970"))

    @property
    def last_online(self) -> datetime.datetime:
        """Date and time when player was last seen online."""
        if self.status.online:
            return datetime.datetime.now(datetime.timezone.utc)
        else:
            return iso8601.parse_date(self._attributes.get("meta", {}).get("lastJoin", "1970"))

    @property
    def online(self) -> bool:
        """Is player online right now, for detailed information see :py:attr:`~status`."""
        return self.status.online

    @property
    def status(self) -> PlayerStatus:
        """Information about player's current online status."""
        return PlayerStatus(self._corkus, self._attributes.get("meta", {}).get("location", {}))

    @property
    def playtime(self) -> PlayerPlaytime:
        """Time that player spent on wynncraft servers."""
        return PlayerPlaytime(self._attributes.get("meta", {}).get("playtime", 0))

    @property
    def combined_level(self) -> int:
        """Combined level of all professions across all characters including combat."""
        return sum(c.combined_level for c in self.characters)

    @property
    def characters(self) -> List[Character]:
        """All of the player's characters."""
        return [Character(self._corkus, self, uuid, char) for uuid, char in self._attributes.get("characters", {}).items()]

    @property
    @deprecated(version="3.0", reason="Use :py:attr:`characters` instead")
    def classes(self) -> List[Character]:
        """All of the player's classes."""
        return self.characters

    @property
    def best_character(self) -> Union[Character, None]:
        """Player's best character. This is determined by sorting by :py:attr:`Character.combat` level and
        :py:attr:`Character.combined_level`."""
        characters = self.characters.copy()
        characters.sort(key = lambda x: (x.combat.level, x.combined_level), reverse = True)
        return characters[0] if len(characters) > 0 else None

    @property
    @deprecated(version="3.0", reason="Use :py:attr:`best_character` instead")
    def best_class(self) -> Union[Character, None]:
        """Player's best class. This is determined by sorting by :py:attr:`Character.combat` level and
        :py:attr:`Character.combined_level`."""
        return self.best_character

    @property
    def member(self) -> Union[PartialMember, None]:
        """Partial representation of player in the guild."""
        if self._attributes.get("guild", {}).get("name", None) is None:
            return None
        else:
            return PartialMember(
                corkus = self._corkus,
                uuid = self.uuid,
                username = self.username,
                guild = self.guild,
                rank = GuildRank(self._attributes.get("guild", {}).get("rank", "RECRUIT"))
            )

    @property
    def guild(self) -> Union[PartialGuild, None]:
        """Partial information about player's guild."""
        if self._attributes.get("guild", {}).get("name", None) is None:
            return None
        else:
            return PartialGuild(self._corkus, self._attributes.get("guild", {}).get("name", ""))

    @property
    def statistics(self) -> PlayerStatistics:
        """General statistics across all characters."""
        return PlayerStatistics(self._corkus, self._attributes.get("global", {}))

    @property
    def quests(self) -> List[Quest]:
        """List of all quests completed by player, combined across all characters."""
        result = []
        for quest in [q for c in self.characters for q in c.quests]:
            if any(q.name == quest for q in result): continue
            result.append(quest)
        return result

    @property
    def dungeons(self) -> List[Dungeon]:
        """List of dungeons completed by this player, combined across all characters."""
        result = []
        for dungeon in [d for c in self.characters for d in c.dungeons]:
            if any(q.name == dungeon for q in result): continue
            result.append(dungeon)
        return result

    @property
    def raids(self) -> List[Raid]:
        """List of raids completed by this player, combined across all characters."""
        result = []
        for raid in [r for c in self.characters for r in c.raids]:
            if any(q.name == raid for q in result): continue
            result.append(raid)
        return result

    @property
    def ranking(self) -> Ranking:
        """Place of player in various leaderboards.

        .. caution::
            This property will return invalid information if player name is
            improperly capitalized.
        """
        return Ranking(self._corkus, self._attributes.get("ranking", {}))

    def __repr__(self) -> str:
        return f"<Player username={self.username!r}>"
