from random import choice

# A tiny lookup the packaging lesson can import as MyPackage.pick.
places = [
    "McDonalds",
    "KFC",
    "Burger King",
    "Taco Bell",
    "Wendys",
    "Arbys",
    "Pizza Hut",
]


def pick():
    """Return a random fast food place."""
    return choice(places)
