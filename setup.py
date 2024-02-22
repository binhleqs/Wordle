from setuptools import setup, find_packages

setup(
name="Wordle",
version="0.1.0",
description="A simple Python package for Word Guessing game",
packages=find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires=">=3.8.9",
)