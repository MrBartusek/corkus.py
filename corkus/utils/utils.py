from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corkus.objects import LogicSymbol

class Utils:
    @staticmethod
    def build_complex_query(symbol: "LogicSymbol", **kwargs: str):
        props = []
        for key, value in kwargs.items():
            if value is None: continue
            props.append(f"{key.lower()}<{value}>")
        if len(props) == 0:
            raise ValueError("at least one keyword argument is reqired for complex search routes")
        return symbol.value + ",".join(props)

    @staticmethod
    def player_to_username(player):
        if isinstance(player, str):
            return player
        elif hasattr(player, "username"):
            username = player.username
            if username is None:
                raise ValueError(f"{type(player)} has username property but it's None")
            return username
        else:
            raise TypeError(f"expected str, Player, PartialPlayer, PartialOnlinePlayer or Member, received {type(player)}")
