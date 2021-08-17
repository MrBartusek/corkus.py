.. _ratelimit:

Rate limit
==========

Rate limit handling is Corkus.py functionality that slows down your
application when hitting API Rate limit. It's completely automated background process that
is enabled by default.

.. tip::

    Current rate limit for Wynncraft API is ``180`` requests per minute across all endpoints.

How it works
~~~~~~~~~~~~

When working with Corkus.py you don't need to worry about rate limit. When you are low on
limit corkus will execute :py:func:`asyncio.sleep` that will delay you request and log that
fact using ``corkus.ratelimit`` logger.

Accessing rate limit
~~~~~~~~~~~~~~~~~~~~

You can access current rate limit information by :py:attr:`Corkus.rate_limit <corkus.Corkus.rate_limit>`

.. autoclass:: corkus.client.RateLimit
    :inherited-members:
