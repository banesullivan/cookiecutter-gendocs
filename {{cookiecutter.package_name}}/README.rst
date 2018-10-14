{{cookiecutter.package_name}}
{% for _ in cookiecutter.package_name %}={% endfor %}

.. image:: https://readthedocs.org/projects/{{cookiecutter.package_name}}/badge/?version=latest
   :target: https://{{cookiecutter.package_name}}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.package_name}}.svg
   :target: https://pypi.org/project/{{cookiecutter.package_name}}/
   :alt: PyPI

.. image:: https://travis-ci.org/{{cookiecutter.github_account}}/{{cookiecutter.package_name}}.svg?branch=master
   :target: https://travis-ci.org/{{cookiecutter.github_account}}/{{cookiecutter.package_name}}
   :alt: Build Status

.. image:: https://img.shields.io/github/stars/{{cookiecutter.github_account}}/{{cookiecutter.package_name}}.svg?style=social&label=Stars
   :target: https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.package_name}}
   :alt: GitHub


{{cookiecutter.description}}



Credits
-------

This package was created with `Cookiecutter`_ and the `banesullivan/cookiecutter-gendocs`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`banesullivan/cookiecutter-gendocs`: https://github.com/banesullivan/cookiecutter-gendocs
