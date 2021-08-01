from datetime import datetime

from .base import CorkusBase
from .partial_guild import PartialGuild
from .territory_location import TeritoryLocation

class Teritory(CorkusBase):
    """Territories are areas which may be claimed by a Guild to receive benefits"""

    @property
    def name(self):
        """The name of the territory"""
        return self.attributes.get("territory", None)

    @property
    def guild(self):
        """Guild that currently holds the territory"""
        guid_name = self.attributes.get("guild", None)
        if guid_name is None or guid_name == "Nobody":
            return None
        else:
            return PartialGuild(self.corkus, guid_name)

    @property
    def acquired(self) -> datetime:
        """Time when the territory was acquired"""
        return datetime.strptime(self.attributes.get("acquired", "1970-01-01 00:00:00"), "%Y-%m-%d %H:%M:%S")

    @property
    def attacker(self):
        """Guild that is currently attacking the territory"""
        guid_name = self.attributes.get("attacker", None)
        if guid_name is None:
            return None
        else:
            return PartialGuild(self.corkus, guid_name)

    @property
    def location(self) -> TeritoryLocation:
        """The name of the territory"""
        return TeritoryLocation(self.corkus, self.attributes.get("location", {}))

    def __repr__(self) -> str:
        return f"<Teritory name={self.name!r} guild={self.guild}>"