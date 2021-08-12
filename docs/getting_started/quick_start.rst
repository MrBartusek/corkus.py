Quick Start
===========

In this section, we go over everything you need to know to start building applications
using Corkus.py, the Python Wynncraft API Wrapper. It's fun and easy. Let's get started.

Prerequisites
-------------

:Python Knowledge:
    You need to know at least a little Python to use Corkus. It's a asynchronous wrapper so
    you need to need basic knowledge how `asyncio`_ work and how to use  ``async`` and ``await``.
    Corkus supports `Python 3.8+`_.
:Wynncraft Knowledge:
    A basic understanding of how Wynncraft works is a must. In the event you
    are not already familiar with Wynncraft start at `Wynncraft Help`_.
:Optional `AIOHTTP`_ Knowledge:
    AIOHTTP is a library that drives Corkus.py and thus understanding how to handle
    ClientSession would be beneficial.

.. _python 3.8+: https://docs.python.org/3/tutorial/index.html

.. _asyncio: https://docs.python.org/3/library/asyncio.html

.. _wynncraft help: https://wynncraft.com/help

.. _aiohttp: https://docs.aiohttp.org


With these prerequisites satisfied, you are ready to learn how to do some of the most
common tasks with Corkus.

Common Tasks
------------

Obtain a :class:`.Corkus` Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need an instance of the :class:`.Corkus` class to do anything with Corkus.py. This is a class
from which you will make all of the request.

.. code-block:: python

    import asyncio
    from corkus import Corkus

    async def main():
        async with Corkus() as corkus:
            pass
            # Do your API stuff here

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

If you are not familiar with `asyncio`_ that snippet may seam a bit scarry. Don't worry!
Thats a minimal requirement to run asynchronous python code! All code that ``main()`` is now asynchronous.

You probably see that this snippet also uses a `Context Manager`_ in order to simplify the code. 
You don't need to use it, this code works exactly the same:

.. code-block:: python

    import asyncio
    from corkus import Corkus

    async def main():
        corkus = Corkus()

        # Do your API stuff here

        await corkus.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

.. _context manager: https://book.pythontips.com/en/latest/context_managers.html

.. note::

    You should use `Context Manager`_ when dealing with smaller scripts and
    manually create :class:`.Corkus` instance when dealing with bots or other
    bigger applications

Obtain a :class:`.Player`
~~~~~~~~~~~~~~~~~~~~~~~~~

TODO