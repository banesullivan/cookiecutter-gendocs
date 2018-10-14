"""{{cookiecutter.module_name}}
{% for _ in cookiecutter.module_name %}-{% endfor %}

This is an example RST docstring for your new module in your new Python package.

Always be sure to define an ``__all__`` list in your modules! Otherwise
``gendocs`` will ignore your code.
"""


__all__ = [
    'FooClass',
]

class FooClass(object):
    """This is an example class"""
    def __init__(self, arg1, arg2):
        self.foo = arg1
        self.boo = arg2

    def run(self, num):
        """Run the Foo algorithm on an input number ``nub``.

        Args:
            num (float): the input object to use

        Return:
            object: The ouput object
        """
        return self.arg1 * num / self.arg2
