{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}


Features
--------

* TODO

Usage
-----

.. code::

   $ {{ cookiecutter.project_slug }} --help

Development
-----------

To see available environments in tox run:

.. code::

   $ tox list

Supply arguments to pytest:

.. code::

   $ tox -e py39 -- --sw

To run pytest manually:

.. code::

   $ pytest

Running the application inside the Python debugger:

.. code::

   $ python -m pdb -m {{ cookiecutter.project_slug }} hello


Credits
-------

This package was created with Cookiecutter_ and the `Cecron/cookiecutter-pycli`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Cecron/cookiecutter-pycli`: https://github.com/Cecron/cookiecutter-pycli
