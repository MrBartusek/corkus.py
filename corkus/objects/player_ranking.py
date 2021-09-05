from __future__ import annotations
from typing import Dict, Union
from .base import CorkusBase
from .enums import ProfessionType

class Ranking(CorkusBase):
    """Represents ranking information of :py:class:`Player`."""
    @property
    def player(self) -> PlayerRanking:
        """Player specific ranking."""
        return PlayerRanking(self._corkus, self._attributes.get("player", {}))

    @property
    def pvp(self) -> None:
        """Pvp ranking of the player.

        .. warning::
            This functionality is not yet implemented intro Wynncraft API and will
            always return ``None``."""
        return self._attributes.get("pvp")

    @property
    def guild(self) -> None:
        """Ranking of player's guild.

        .. warning::
            This functionality is not yet implemented intro Wynncraft API and will
            always return ``None``.
        """
        return self._attributes.get("guild")

class PlayerRanking(CorkusBase):
    """Represents player-specific :py:class:`Ranking` information."""
    @property
    def solo(self) -> PlayerSoloRanking:
        """Solo ranking."""
        return PlayerSoloRanking(self._corkus, self._attributes.get("solo", {}))

    @property
    def overall(self) -> PlayerOverallRanking:
        """Overall ranking."""
        return PlayerOverallRanking(self._corkus, self._attributes.get("overall", {}))

class PlayerSoloRanking(CorkusBase):
    """Represents *solo* category of :py:class:`PlayerRanking`."""
    @property
    def combat(self) -> Union[int, None]:
        """Shortcut to combat in :py:attr:`professions`."""
        return self._attributes.get("combat")

    @property
    def professions(self) -> Dict[ProfessionType, Union[int, None]]:
        """Dictionary containing all of the :py:class`ProfessionType` as keys and
        player's places in these leaderboards as keys. Keys are ``None`` if not in top 100."""
        result = {}
        for prof in ProfessionType:
            result[prof] = self._attributes.get(prof.value.lower())
        return result

    @property
    def overall(self) -> Union[int, None]:
        """Player's place in overall solo leaderboard. Returns ``None`` if not in top 100."""
        return self._attributes.get("overall")

class PlayerOverallRanking(CorkusBase):
    """Represents *overall* category of :py:class:`PlayerRanking`."""
    @property
    def all(self) -> Dict[ProfessionType, Union[int, None]]:
        """Player's place in overall all leaderboard. Returns ``None`` if not in top 100."""
        return self._attributes.get("all")

    @property
    def professions(self) -> Union[int, None]:
        """Player's place in overall professions leaderboard. Returns ``None`` if not in top 100."""
        return self._attributes.get("profession")

    @property
    def combat(self) -> Union[int, None]:
        """Player's place in overall combat leaderboard. Returns ``None`` if not in top 100."""
        return self._attributes.get("combat")
