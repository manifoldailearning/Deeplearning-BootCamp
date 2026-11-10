# A directory is importable as a package when it contains this file.
# These imports are what `from MyPackage import add, multiply, pick` exposes.

from .math.add_multiply import add, multiply
from .fast_food import pick

__all__ = ["add", "multiply", "pick"]
