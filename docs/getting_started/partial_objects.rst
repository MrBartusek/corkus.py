.. _partial_objects:

Partial Objects
===============

.. py:currentmodule:: corkus.objects

What are Partial Objects
~~~~~~~~~~~~~~~~~~~~~~~~

Some of the objects in Corkus.py are marked as ``Partial``. For example:
:py:class:`PartialPlayer`, :py:class:`PartialGuild` or :py:class:`PartialIngredient`.
These objects doesn't contain a lot of information and their primary use is to
allow for easy access to other API resources simplifying your code.

Take for example :py:func:`GuildEndpoint.list_all <corkus.endpoints.GuildEndpoint.list_all>`. This function lists all of the
guilds on the server, there are ``12,000+`` of those. In the ideal world this function
would return :py:class:`List <typing.List>` [:py:class:`Guild`] hoverer that is not the
case. This would significantly slow the API. So instead it returns
:py:class:`List <typing.List>` [:py:class:`str`]. Raw response looks something like that:

.. code-block:: json

    {
        "guilds": [
            "WynnContentTeam",
            "Holders Of LE",
            "Wynn Theory",
            "The Red Warrior",
            "Nanite Systems"
        ]
    }

Corkus instead of representing that as :py:class:`List <typing.List>` [:py:class:`str`]
wraps it intro :py:class:`List <typing.List>` [:py:class:`PartialGuild`]. You can still
use it as a normal string using :py:class:`PartialGuild.name` but, you can also
use :py:func:`PartialGuild.fetch` to convert it to :py:class:`Guild`.

``fetch()`` function
~~~~~~~~~~~~~~~~~~~~

Every ``Partial`` object has some sort of ``async fetch()`` function.
These functions are shortcuts for calls using Endpoints. For example:
Let's say that you want to get ``level`` of first guild in
:py:func:`GuildEndpoint.list_all <corkus.endpoints.GuildEndpoint.list_all>`.

.. admonition:: Bad Practice
    :class: error

    .. code-block:: python

        all_guilds = await corkus.guild.list_all()
        guild_name = all_guild[0].name
        guild = await corkus.guild.get(guild_name)

        print(guild.level) # => 27

    Don't do that! You can simplify this code using :py:func:`PartialGuild.fetch`!

.. admonition:: Good Practice
    :class: tip

    .. code-block:: python

        all_guilds = await corkus.guild.list_all()
        guild = await all_guild[0].fetch()

        print(guild.level) # => 27

    This snippet use :py:func:`PartialGuild.fetch` to make code more readable and faster to
    write.

Every ``fetch()`` is a API call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to understand that calling ``fetch()`` is a web request to
Wynncraft API, that means it will take a second depending how fast your
internet speed is. You generally should minimize number of calls to seed up
your app and don't abuse the API too much. So instead of calling
:py:func:`PlayerEndpoint.search <corkus.endpoints.PlayerEndpoint.search>`
and fetching each player, maybe you can just cope with their usernames?

.. admonition:: Remember

   Don't over-use ``fetch()`` functions.
