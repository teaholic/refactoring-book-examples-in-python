from setuptools import setup, find_packages

setup(
    name="refactoring-examples",
    version="0.0.1",
    description="Refactoring book examples (2nd edition) in Python",
    author="@teaholic",
    long_description_content_type="text/markdown",
    classifiers=["Development Status :: 3 - Alpha",],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[],
    extras_require={"test": ["tox==3.27.0"]},
)
