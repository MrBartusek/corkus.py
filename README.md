![corkus banner](https://i.imgur.com/8FjYte1.gif)


[![build](https://img.shields.io/github/workflow/status/MrBartusek/corkus.py/build)](https://github.com/MrBartusek/corkus.py/actions) [![codecov](https://codecov.io/gh/MrBartusek/corkus.py/branch/main/graph/badge.svg?token=oZbLlhqRKJ)](https://codecov.io/gh/MrBartusek/corkus.py) [![Documentation Status](https://img.shields.io/readthedocs/corkuspy)](https://corkuspy.readthedocs.io/en/latest/?badge=latest) [![PyPI](https://img.shields.io/pypi/v/corkus.py)](https://pypi.org/project/corkus.py/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/corkus.py)](https://pypi.org/project/corkus.py/)

# Corkus.py ⚙️

Asynchronous, feature-rich and easy to use Python wrapper for [Public Wynncraft API](https://docs.wynncraft.com).

## Key Features

- Asynchronous API using `async` and `await`
- Easy to use with an object oriented design and `fetch` functions
- ≈ 95% coverage of the Wynncraft API as of now
- Proper rate limit handling
- Responses caching

## Missing Features

- Item Database Endpoint
- Wired search routes
- Error handling

## Installation

*Python 3.8+ or higher is required*

```shell
pip install corkus.py
```

Or install latest development version:

```shell
pip install --upgrade  git+https://github.com/MrBartusek/corkus.py@main
```

See [documentation](https://corkuspy.readthedocs.io/en/latest/getting_started/installation.html) for more information.

## Quick Example

Using [Context Manager](https://book.pythontips.com/en/latest/context_managers.html):

```python
import asyncio
from corkus import Corkus

async def player_stats():
    async with Corkus() as corkus:
        player = await corkus.player.get("Salted")
        print(f"username: {player.username}")
        print(f"chests_found: {player.statistics.chests_found}")

loop = asyncio.get_event_loop()
loop.run_until_complete(player_stats())
```

Without Context Manager:

```python
import asyncio
from corkus import Corkus

async def player_stats():
    corkus = Corkus()

    player = await corkus.player.get("Salted")
    print(f"username: {player.username}")
    print(f"chests_found: {player.statistics.chests_found}")

    await corkus.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(player_stats())
```

Output:
```
username: Salted
chests_found: 219
```