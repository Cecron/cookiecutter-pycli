==================
cookiecutter-pycli
==================

Cookiecutter_ template for a Python package.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

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

Development
-----------

To test this template during development, use pytest::

    pytest
