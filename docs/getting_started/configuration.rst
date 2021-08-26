.. _configuration:

Configuring Corkus
==================

Corkus can be configured through the use of keyword arguments when initializing instances of
``Corkus``. All of the Configuration Options can be specified using a keyword argument of the
same name. For example:

.. code-block:: python

    corkus = Corkus(
        timeout = 10,
        cache_enable = False
    )

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

timeout
    Default: ``30``

    Number of seconds after API requests will raise :py:exc:`corkus.errors.CorkusTimeoutError`. It can be
    overridden by timeout argument in each API call function.

session
    If you want to use a custom `ClientSession <https://docs.aiohttp.org/en/latest/client_reference.html#aiohttp.ClientSession>`_,
    you can pass it in the following argument.

cache_enable
    Default: ``True``

    Should :ref:`cache` be enabled.

ratelimit_enable
    Default: ``True``

    Should :ref:`ratelimit` be enabled. **It's highly recommended to keep this option enabled!**
