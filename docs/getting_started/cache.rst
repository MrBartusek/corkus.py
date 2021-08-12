Response Caching
================

.. py:currentmodule:: corkus.endpoints

Response Caching is Corkus.py functionality that speeds up your application
and decrees load on the API. It's completely automated background process that
is enabled by default.

Response caching time
~~~~~~~~~~~~~~~~~~~~~

The time for which Corkus caches responses is purely bases on 
`Cache-Control <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control>`_
header sent by the API. Header is provided for most of the endpoints,
if not, it defaults to 10 minutes.

.. important::

    Caching times are regulated by API administrators and are subject to change independently of Corkus.py.

Current cache times are decided intro 3 groups:

:Short Cache ``30 seconds``:
    This group is designated for most rapidly changing endpoints.

    - :py:func:`GuildEndpoint.list_all`
    - :py:func:`GuildEndpoint.get`
    - :py:func:`TerritoryEndpoint.list_all`
    - :py:func:`NetworkEndpoint.players_sum`
    - :py:func:`NetworkEndpoint.servers_list`
    - :py:func:`SearchEndpoint.guilds_and_players`
    - :py:func:`PlayerEndpoint.search`
    - :py:func:`GuildEndpoint.search`
    - :py:func:`LeaderboardEndpoint.guild`
    - :py:func:`LeaderboardEndpoint.combat`
    - :py:func:`LeaderboardEndpoint.pvp`

:Medium Cache ``10 minutes``:
    This group is designated for less active endpoints that still update sometimes.

    - :py:func:`PlayerEndpoint.get`
    - :py:func:`PlayerEndpoint.get_uuid`
    - :py:func:`IngredientEndpoint.list_all`
    - :py:func:`RecipeEndpoint.list_all`

:Long Cache ``60 minutes``:
    This group is designated for mostly static endpoints that change only on updates.

    - :py:func:`IngredientEndpoint.get`
    - :py:func:`RecipeEndpoint.get_by_id`

Accessing cache
~~~~~~~~~~~~~~~

.. py:currentmodule:: corkus

See: :py:attr:`CorkusCache`
