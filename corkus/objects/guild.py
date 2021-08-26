from __future__ import annotations
from .member import Member
from typing import List
from .base_guild import BaseGuild

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

    def __repr__(self) -> str:
        return f"<Guild tag={self.tag!r} name={self.name!r}>"
