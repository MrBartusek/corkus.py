from __future__ import annotations
from .base import CorkusBase
from .partial_teritories import PartialTeritories
from datetime import datetime
from iso8601 import iso8601
from .guild_banner import GuildBanner

class BaseGuild(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the guild."""
        return self._attributes.get("name", "")

    @property
    def tag(self) -> str:
        """Prefix displayed as a shorter 3 or 4 letters representation of guild.
        Like ``AVO``, ``ERN`` or ``YIN``. It's mostly upper-case but it's not a requirement.
        It's unique across all guild.
        """
        return self._attributes.get("prefix", "")

    @property
    def created(self) -> datetime:
        """Datetime when guild was created."""
        return iso8601.parse_date(self._attributes.get("created", "1970"))

    @property
    def level(self) -> int:
        """Level of the guild from ``1`` to ``100``. Guild members can use ``/guild xp`` command
        to contribute XP to the guild. Leveling guild grants perks like more
        member slots or guild bank upgrades. The exact XP values are available
        `on the wiki <https://wynncraft.fandom.com/wiki/Guilds#Leveling_Guild>`_.
        """
        return self._attributes.get("level", 1)

    @property
    def territories(self) -> PartialTeritories:
        """Teritories owned by the guild throughout wars."""
        return PartialTeritories(
            corkus = self._corkus,
            guild = self,
            count = self._attributes.get("territories", 0)
        )

    @property
    def banner(self) -> GuildBanner:
        """Information about appearance of guild banner and it's tier."""
        return GuildBanner(self._corkus, self._attributes.get("banner", {}))

    def __repr__(self) -> str:
        return f"<BaseGuild tag={self.tag!r} name={self.name!r}>"
