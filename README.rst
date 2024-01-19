==================
cookiecutter-pycli
==================

Cookiecutter_ template for a Python package using Poetry_, Sphinx_ and Tox_.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Poetry: https://python-poetry.org/docs
.. _Sphinx: https://www.sphinx-doc.org
.. _Tox: https://tox.wiki

Usage
-----

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pipx install cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/Cecron/cookiecutter-pycli.git

Or use Cruft_ instead of Cookiecutter::

    cruft create https://github.com/Cecron/cookiecutter-pycli.git

Now you can update the project with newer versions of the template::

    cruft update

.. _Cruft: https://github.com/Cecron/cookiecutter-pycli.git

Initialize everything in yyour new project directory with poetry::

    poetry install
    . .venv/bin/activate
    tox


Development
-----------

To test this template during development, use pytest::

    pytest
