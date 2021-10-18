.. _search:
.. py:currentmodule:: corkus.objects
.. role:: green
.. role:: yellow
.. role:: red

Search Routes
=============

Wynncraft API uses a quite unique system for searching things. All of the search routes
are divided intro 3 categories:

:green:`Simple`
    Simple queries perform simple pattern matching and display results. These are just
    regular function calls.

    Example:

    .. code-block:: python

        await corkus.ingredient.search_by_level(30)



:yellow:`Moderate`
    Moderate queries introduce conditionality for more advanced searches. The only concept
    that you need to understand are :py:class:`LogicSymbol`

    Example:

    .. code-block:: python

        await corkus.ingredient.search_by_professions(
            LogicSymbol.AND,
            [ProfessionType.WOODWORKING, ProfessionType.ALCHEMISM]
        )

:red:`Complex`
    Complex queries allow to search for specific fields in the objects. For these searches
    you need to use both :py:class:`LogicSymbol` and keyword arguments.

    Example:

    .. code-block:: python

        await corkus.ingredient.search_by_item_modifiers(
            LogicSymbol.AND,
            durability = -20,
            strength = 20
        )
