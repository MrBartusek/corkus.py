.. _keys:

API Keys
========

Every user of the API is heavily encouraged to get API key(s) for their application(s).
They are mainly used for increasing ratelimit and better API management.

API Keys are not required to use the API. The base rate limit is 180 req / min per IP.
Overtime non-key rate limit will be lowered but, you won't be required to use a key as
long as you are within the rate limit.

Applying for an API Key
~~~~~~~~~~~~~~~~~~~~~~~

Fill this application out, send a private message to ``@colin350`` on the
`forums <https://forums.wynncraft.com/>`_. You might be asked additional questions.

.. note::
    Have in mind that you are most likely using :ref:`cache`. So, you should accordingly
    respond to the cache question.

.. code-block::

    Application Name:
    Author(s) Name(s) (Minecraft in-game name):
    Website link(s) to your application (e.g. GitHub, Forums, etc.):
    Contact Information (i.e. what is the fastest/easiest way we can get in contact with you? Please do not list phone numbers, please list at least 2 different ways to get in contact):
    Description of the Application:
    How you are currently using / planning to use our API service:
    Do you request the API in frontend code or from a backend server?
    Do you cache parts of the API, if so, what?
    How big is your audience (i.e how many players use your application)?
    What are you doing with player's data? (e.g. why do you request it, what computations are done on it, how is it stored, what is stored, etc.)

Using the API key
~~~~~~~~~~~~~~~~~

.. py:currentmodule:: corkus

When you have obtained API key you can provide it as an argument to the :py:func:`Corkus.start() <Corkus.start>` function
like so:

.. code-block:: python

    await corkus.start("API_KEY")

