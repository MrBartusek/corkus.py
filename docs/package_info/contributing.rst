Contributing to Corkus.py
=========================

As an open source project, Corkus.py welcomes contributions in many forms. 
We greatly appreciate any work contributed, no matter how small!

Pull Request Process
--------------------

If you want to make a code contribution please make a pull request against ``main`` branch.

Local Setup
~~~~~~~~~~~

Clone this repo to wherever you want:

.. code-block:: bash

    git clone https://github.com/MrBartusek/corkus.py.git

Go into the repo folder:

.. code-block:: bash

    cd corkus.py

Install dependencies:

.. code-block:: bash

    pip install -r requirements.txt
    pip install -r requirements-dev.txt

Testing
~~~~~~~

We want to keep the project coverage as high as possible. Your PR should include tests
if they are needed and pass all of the existing ones.

`Github Actions <https://github.com/MrBartusek/corkus.py/actions/workflows/main.yml>`_ run
tests for each PR but, if you want to run them by yourself you can use following command:

.. code-block:: bash

    python -m unittest discover

Linting
~~~~~~~

Corkus uses PyLint to ensure consistent code style. In order for your PR to be accepted it must pass
linting checks.

`Github Actions <https://github.com/MrBartusek/corkus.py/actions/workflows/main.yml>`_ run
linting for each PR but, if you want to run it by yourself you can use following command:

.. code-block:: bash

    python -m pylint corkus tests

Documentation
~~~~~~~~~~~~~

Documentation setup:

.. code-block:: bash

    cd docs
    pip install -r requirements.txt

Building documentation:

.. code-block:: bash

    make html

Builded documentation is available under ``docs/_build/html``
