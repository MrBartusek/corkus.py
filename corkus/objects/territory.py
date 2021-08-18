from __future__ import annotations
from datetime import datetime
from typing import Union

from .base import CorkusBase
from .partial_guild import PartialGuild
from .territory_location import TerritoryLocation

class Territory(CorkusBase):
    """Territories are areas which may be claimed by a :py:class:`Guild` to receive benefits."""

    @property
    def name(self) -> str:
        """The name of the territory."""
        return self._attributes.get("territory", None)

    @property
    def guild(self) -> Union[PartialGuild, None]:
        """Guild that currently holds the territory."""
        guid_name = self._attributes.get("guild", None)
        if guid_name is None or guid_name == "Nobody":
            return None
        else:
            return PartialGuild(self._corkus, guid_name)

    @property
    def acquired(self) -> datetime:
        """Datetime when the territory was acquired."""
        return datetime.strptime(self._attributes.get("acquired", "1970-01-01 00:00:00"), "%Y-%m-%d %H:%M:%S")

    @property
    def attacker(self) -> Union[PartialGuild, None]:
        """Guild that is currently attacking the territory."""
        guid_name = self._attributes.get("attacker", None)
        if guid_name is None:
            return None
        else:
            return PartialGuild(self._corkus, guid_name)

    @property
    def is_attacked(self) -> bool:
        """Is this territory currently under attack."""
        return self.attacker is not None

    @property
    def location(self) -> TerritoryLocation:
        """The location of this territory."""
        return TerritoryLocation(self._corkus, self._attributes.get("location", {}))

    def __repr__(self) -> str:
        return f"<Territory name={self.name!r} guild={self.guild}>"
