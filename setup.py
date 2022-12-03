from distutils.core import setup
from setuptools import find_packages

setup(
    name = "snowflake",
    version = "0.1",
    author = "udayvarun",
    author_email = "kothapalliudayvarun@gmail.com"
    packages = find_packages(),
    install_requires = ["numpy", "turtles"],
)
