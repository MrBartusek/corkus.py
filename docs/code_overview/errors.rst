Corkus Exceptions
=================

.. py:currentmodule:: corkus.errors

Exceptions hierarchy:

- :py:exc:`CorkusException`

  - :py:exc:`InvalidInputError`
  - :py:exc:`HTTPError`

    - :py:exc:`WynncraftServerError`
    - :py:exc:`RatelimitExceeded`
    - :py:exc:`BadRequest`
  
  - :py:exc:`CorkusTimeoutError`

.. automodule:: corkus.errors
  :inherited-members:
  :show-inheritance: