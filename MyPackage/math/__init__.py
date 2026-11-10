# math/ is a subpackage. Importing MyPackage.math loads this file.
from .add_multiply import add, multiply

__all__ = ["add", "multiply"]
