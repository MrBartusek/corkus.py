# type: ignore

from .client import Corkus
from corkus.version import __version__

import warnings
warnings.warn("corkus.py is deprecated", DeprecationWarning)