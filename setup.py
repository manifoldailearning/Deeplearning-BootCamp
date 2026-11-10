from setuptools import find_packages, setup

# Editable install from this folder: pip install -e .
# Then, in Python: from MyPackage import add, multiply, pick
setup(
    name="MyPackage",
    version="0.2",
    description="First package created for the deep learning course",
    url="https://github.com/manifoldailearning/Deeplearning-BootCamp",
    author="Manifold AI Learning",
    author_email="support@manifoldailearning.in",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    zip_safe=False,
)
