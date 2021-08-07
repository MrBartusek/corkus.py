![corkus banner](https://i.imgur.com/8FjYte1.gif)


[![build](https://github.com/MrBartusek/corkus.py/actions/workflows/main.yml/badge.svg)](https://github.com/MrBartusek/corkus.py/actions) [![codecov](https://codecov.io/gh/MrBartusek/corkus.py/branch/main/graph/badge.svg?token=oZbLlhqRKJ)](https://codecov.io/gh/MrBartusek/corkus.py) [![PyPI](https://img.shields.io/pypi/v/corkus.py)](https://pypi.org/project/corkus.py/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/corkus.py)](https://pypi.org/project/corkus.py/)

# Corkus.py ⚙️

Asynchronous modern, feature-rich and easy to use Python wrapper for [Public Wynncraft API](https://docs.wynncraft.com).

## Key Features

- Asynchronous API using `async` and `await`
- Easy to use with an object oriented design and `fetch` functions
- ≈ 80% coverage of the Wynncraft API as of now
- ~~Responses caching~~ Soon
- ~~Proper rate limit handling~~ Soon

## Missing Features

- Recipe Endpoint
- Item Database Endpoint
- Ingredients Search
- Proper rate limit handling
- Responses caching
- Error handling

## Installation

*Python 3.8+ or higher is required*

```shell
pip install corkus.py
```

## Quick Example

```python
import asyncio
from corkus import Corkus

async def player_stats():
    corkus = Corkus()

    player = await corkus.player.get("Salted")
    print(player.statistics.chests_found) # => 219

    await corkus.close()

asyncio.get_event_loop().run_until_complete(player_stats())
```
