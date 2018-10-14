"""``{{cookiecutter.package_name}}``: {{cookiecutter.description}}
"""

import setuptools

__version__ = '0.0.0'

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="{{cookiecutter.package_name}}",
    version=__version__,
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.package_name}}",
    packages=setuptools.find_packages(),
    install_requires=[
        # TODO: add dependencies
    ],
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
    ),
)
