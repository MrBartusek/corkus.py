Quick Start
===========

In this section, we go over everything you need to know to start building applications
using Corkus.py, the Python Wynncraft API Wrapper. It's fun and easy. Let's get started.

Prerequisites
-------------

:Python Knowledge: You need to know at least a little Python to use Corkus. It's a asynchronous wrapper so
    you need to have basic knowledge how `asyncio`_ work and how to use  ``async`` and ``await`` syntax.
    Corkus supports `Python 3.8+`_.
:Wynncraft Knowledge: A basic understanding of how Wynncraft works is a must. In the event you
    are not already familiar with Wynncraft start at `Wynncraft Help`_.
:Optional `AIOHTTP`_ Knowledge: AIOHTTP is a library that drives Corkus.py and thus understanding how to handle
    ClientSession would be beneficial.

.. _python 3.8+: https://docs.python.org/3/tutorial/index.html

.. _asyncio: https://docs.python.org/3/library/asyncio.html

.. _wynncraft help: https://wynncraft.com/help

.. _aiohttp: https://docs.aiohttp.org


With these prerequisites satisfied, you are ready to learn how to do some of the most
common tasks with Corkus.

Example usage
--------------------

This guide gives a brief introduction to the Corkus.py. It assumes you have the library installed.
If you don’t, check the :ref:`install`.

This is a simple application for fetching player statistics:

.. code-block:: python

    import asyncio
    from corkus import Corkus

    async def main():
        async with Corkus() as corkus:

            player = await corkus.player.get("MrBartusekXD")
            print(f"username: {player.username}")
            character = player.best_character
            print(f"best character: {character.display_name} ({character.combat.level}lv)")

            if player.guild:
                guild = await player.guild.fetch()
                print(f"guild: {player.guild.name} {guild.level}lv ({len(guild.members)} members)")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

This will print something like that:

.. code-block::

    username: MrBartusekXD
    best character: Mage (102lv)
    guild: The Farplane 63lv (60 members)

If you are not familiar with `asyncio`_ that snippet may seam a bit scarry. Don't worry!
Thats a minimal requirement to run asynchronous Python code! All code inside ``main()`` is
now asynchronous.

You probably see that this snippet also uses a `Context Manager`_ in order to simplify the code. 
You don't need to use it, this code works exactly the same:

.. code-block:: python

    import asyncio
    from corkus import Corkus

    async def main():
        corkus = Corkus()

        player = await corkus.player.get("MrBartusekXD")
        print(f"username: {player.username}")
        character = player.best_character
        print(f"best character: {character.display_name} ({character.combat.level}lv)")

        if player.guild:
            guild = await player.guild.fetch()
            print(f"guild: {player.guild.name} {guild.level}lv ({len(guild.members)} members)")

        await corkus.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

.. _context manager: https://book.pythontips.com/en/latest/context_managers.html

In this example you need to call :py:func:`Corkus.start() <corkus.Corkus.start>` and
:py:func:`Corkus.close() <corkus.Corkus.close>`. These are two lifecycle function that needs
to always be called at the start and end of your application.

.. note::

    You should use `Context Manager`_ when dealing with smaller scripts and directly
    create and close :class:`.Corkus` instance when dealing with bots or other
    bigger applications.
