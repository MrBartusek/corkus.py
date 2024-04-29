Corkus.py - Wynncraft API Wrapper
==================================

.. image:: https://i.imgur.com/8FjYte1.gif

Corkus.py is a asynchronous, feature-rich and easy to use Python wrapper for `Public Wynncraft API <https://docs.wynncraft.com>`_.

.. danger::

        **Corkus.py is no longer maintained**

        Due to recent changes in the Wynncraft API, Corkus.py is no longer working and will not receive further updates or support. Some endpoints based on the v2 API may still be operational, but those relying on the now-removed v1 API and new v3 API are no longer functioning. Additionally, more features may become broken in the future.

        I'm unable to recommend any other Python-based wrapper for the Wynncraft API - I don't see any good alternatives. It is strongly advised to not use this project anymore due to its outdated and non-functional state.

        Thank you to all users and contributors for your support and feedback throughout the lifespan of this project.


.. py:currentmodule:: corkus.objects

Key Features
------------

- Modern asynchronous API using ``async/await`` syntax
- Easy to use with an object oriented design using fetch and helper functions
- 100% coverage of the Wynncraft API
- Proper rate limit handling that prevents 429s
- Responses caching to improve speed

Installation
------------

.. card:: Install Corkus.py
    :link: install
    :link-type: ref

    Navigate to the installation guide. You will learn how to
    install the newest version of Corkus.py

Quickstart
------------

.. card:: Start using Corkus.py
    :link: quickstart
    :link-type: ref

    Navigate to the quickstart guide. You will make your first application
    using Corkus.py

Documentation
-------------

Corkus documentation is organized into the following sections:

.. toctree::
    :maxdepth: 1
    :caption: Getting Started

    getting_started/installation
    getting_started/quick_start
    getting_started/discord
    getting_started/api_keys
    getting_started/configuration
    getting_started/ratelimit
    getting_started/cache
    getting_started/partial_objects
    getting_started/search_routes

.. toctree::
    :maxdepth: 1
    :caption: Code Overview

    code_overview/corkus_client
    code_overview/endpoints
    code_overview/corkus_objects
    code_overview/errors

.. toctree::
    :maxdepth: 1
    :caption: Package Info

    package_info/change_log
    package_info/contributing
    GitHub Repository <https://github.com/MrBartusek/corkus.py>
    Forum Post <https://forums.wynncraft.com/threads/corkus-py-python-wrapper-for-wynncraft-api.295400/>
    PyPI Package <https://pypi.org/project/corkus.py/>

.. toctree::
    :hidden:

    genindex
