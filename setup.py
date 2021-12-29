from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="tusc",
    version="0.0.2",
    author="Lucas H. McCabe",
    author_email="lucasmccabe@gwu.edu",
    description="a Python library providing tools for combinatorial maths",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasmccabe/tusc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
