from corkus.objects import LogicSymbol

class Utils:
    @staticmethod
    def build_complex_query(symbol: LogicSymbol, **kwargs: str):
        props = []
        for key, value in kwargs.items():
            if value is None: continue
            props.append(f"{key.lower()}<{value}>")
        if len(props) == 0:
            raise ValueError("at least one keyword argument is reqired for complex search routes")
        return symbol.value + ",".join(props)
