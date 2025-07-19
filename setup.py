from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel-Project",
    version="0.1",
    author="Kennedy",
    packages= find_packages(),
    install_requires=requirements,
)
