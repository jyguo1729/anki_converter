from setuptools import setup

setup(
    name="langlib",
    version="0.1",
    description="A Python package for lanugage learning",
    author="Jiayin Guo",
    packages=["langlib"],
    console_scripts=["scripts/dictgen.py"],
    install_requires=[
        "numpy",
        "pandas",
    ],
)
