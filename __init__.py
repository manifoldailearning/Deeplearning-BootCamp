# Does two things
# The Python interpreter recognizes a folder as the package if it contains __init__.py file. (prior to Python 3.5
# __init__.py exposes specified resources from its modules to be imported.

from .math.add_multiply import add,multiply
from .fast_food import pick

