![corkus banner](https://i.imgur.com/8FjYte1.gif)

[![pypi](https://img.shields.io/pypi/v/corkus.py)](https://pypi.org/project/corkus.py/)
[![build](https://img.shields.io/github/workflow/status/MrBartusek/corkus.py/build)](https://github.com/MrBartusek/corkus.py/actions)
[![docs build](https://img.shields.io/readthedocs/corkuspy)](https://corkuspy.readthedocs.io/en/stable)
[![Codecov](https://img.shields.io/codecov/c/github/MrBartusek/corkus.py)](https://app.codecov.io/gh/MrBartusek/corkus.py)
[![python version](https://img.shields.io/pypi/pyversions/corkus.py)](https://pypi.org/project/corkus.py/)
![downloads](https://img.shields.io/pypi/dm/corkus.py?color=sucess)

# Corkus.py ⚙️

Asynchronous, feature-rich and easy to use Python wrapper for [Public Wynncraft API](https://docs.wynncraft.com).

## Key Features

- Modern asynchronous API using `async`/`await` syntax.
- Easy to use with an object oriented design using `fetch` and helper functions.
- 100% coverage of the Wynncraft API.
- Proper rate limit handling that prevents 429s.
- Responses caching to improve speed.

## Installation

*Python 3.8+ or higher is required*

```shell
pip install corkus.py
```

Or install latest development version:

```shell
pip install --upgrade git+https://github.com/MrBartusek/corkus.py@main
```

See [documentation](https://corkuspy.readthedocs.io/en/stable/getting_started/installation.html) for more information.

## Quick Example

Using [Context Manager](https://book.pythontips.com/en/latest/context_managers.html):

```python
import asyncio
from corkus import Corkus

async def player_stats():
    async with Corkus() as corkus:
        player = await corkus.player.get("MrBartusekXD")
        character = player.best_character
        print(f"username: {player.username}")
        print(f"best character: {character.display_name} ({character.combat.level}lv)")

loop = asyncio.get_event_loop()
loop.run_until_complete(player_stats())
```

Without Context Manager:

```python
import asyncio
from corkus import Corkus

async def player_stats():
    corkus = Corkus()
    await corkus.start()

    player = await corkus.player.get("MrBartusekXD")
    character = player.best_character
    print(f"username: {player.username}")
    print(f"best character: {character.display_name} ({character.combat.level}lv)")

    await corkus.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(player_stats())
```

Output:
```
username: MrBartusek
best character: Mage (102lv)
```

## Contributing

Want to contribute to the project?

First of all, thanks! Check [contributing guidelines](https://corkuspy.readthedocs.io/en/stable/package_info/contributing.html) for more information.

## Links
- [Documentation](https://corkuspy.readthedocs.io)
- [Forum Post](https://forums.wynncraft.com/threads/corkus-py-python-wrapper-for-wynncraft-api.295400/)
- [PyPi Package](https://pypi.org/project/corkus.py/)
