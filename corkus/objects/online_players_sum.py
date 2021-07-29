from objects import CorkusBase

class OnlinePlayersSum(CorkusBase):
    @property
    def players_sum(self) -> int:
        return self.attributes.get("players_online", 0)

    def __int__(self) -> int:
        return self.players_sum