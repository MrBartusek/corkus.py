.. _configuration:

Configuring Corkus
==================

Corkus can be configured through the use of keyword arguments when initializing instances of
``Corkus``. All of the Configuration Options can be specified using a keyword argument of the
same name. For example:

.. code-block:: python

    corkus = Corkus(
        timeout = 10,
        disable_cache = False
    )

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

timeout
    Default: ``60``

    Number of seconds after which API requests will raise :py:exc:`corkus.errors.CorkusTimeoutError`. It can be
    overridden by timeout argument in each API call function.

disable_cache
    Default: ``False``

    Disable :ref:`cache` module. No request will be saved on disc, this may slow down the client.

disable_ratelimit
    Default: ``False``

    Disable :ref:`ratelimit` module. Request won't be slowed down while approaching the rate limit. This may cause
    :py:exc:`corkus.errors.RatelimitExceeded` errors. 

    .. danger::

        IPs that repeatedly exceed the rate limit could be blacklisted.
