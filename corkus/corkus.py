from typing import Optional
from corkus.utils.constants import TIMEOUT
from corkus.utils.request import CorkusRequest

from corkus.endpoints.network import Network

class Corkus:
    """First-class interface for accessing Wynncraft API"""

    def __init__(self, *, timeout: Optional[int] = None) -> None:
        if timeout is None:
            timeout = TIMEOUT
        self.request = CorkusRequest(timeout)
        self.network = Network(self)
