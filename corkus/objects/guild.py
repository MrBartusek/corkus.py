from __future__ import annotations

from corkus.utils.utils import Utils
from .member import Member
from typing import List, Union, TYPE_CHECKING
from .base_guild import BaseGuild

if TYPE_CHECKING:
    from .player import Player
    from .partial_player import PartialPlayer
    from .partial_online_player import PartialOnlinePlayer

class Guild(BaseGuild):
    """`Guilds <https://wynncraft.fandom.com/wiki/Guilds>`_ are Wynncraft communities of people
    that work together to achieve their goals.
    """
    @property
    def members(self) -> List[Member]:
        """List of all members currently in guild."""
        return [Member(self._corkus, self , m) for m in self._attributes.get("members", [])]

    @property
    def level_progress(self) -> float:
        """Progress to next :py:attr:`level` in precentage 0-100%

        .. caution::
            This property is currently bugged and return invalid precentage. See:
            `Wynncraft/WynncraftAPI#61 <https://github.com/Wynncraft/WynncraftAPI/issues/61>`_.
        """
        return self._attributes.get("xp", 0)

    def get_member(self, player: Union[str, Player, PartialPlayer, PartialOnlinePlayer, Member]) -> Union[Member, None]:
        """Get member of the guild from player. Returns `None` if player is not in guild.

        :param player: Player username or player object to check for.
        """
        username = Utils.player_to_username(player)
        return any(m for m in self.members if m.username == username)

    def __repr__(self) -> str:
        return f"<Guild name={self.name!r} tag={self.tag!r} members={len(self.members)}>"
