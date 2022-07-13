from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_variable(variable_name, *file_paths):
    """
    Returns the value of a variable assignment in a
    file path where the format is 'variable_name = VALUE'.
    """
    file_name = read(*file_paths)
    match = re.search(rf"^{variable_name} = ['\"]([^'\"]*)['\"]",
                      file_name, re.M)
    if match:
        return match.group(1)
    raise RuntimeError(f"Unable to find {variable_name}.")


NAME = find_variable("__app_name__", "ggcli", "__init__.py")
VERSION = find_variable("__version__", "ggcli", "__init__.py")
DESCRIPTION = 'CLI application.'
LONG_DESCRIPTION = 'A package that allows the user to increase their productivity with day to day tasks.'

setup(
    name=NAME,
    version=VERSION,
    author="Brenden Vogt",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[],
    # important: important for executing this package as a command line tool
    scripts=["bin/ggcli"],
    python_requires=">= 3.6",
    keywords=['cli', 'productivity'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    # important: links local packages together for runtime
    packages=find_packages(exclude=['tests*']),
    entry_points={  # either use scripts or use entry_point
        "console_scripts": [
            "ggcli = ggcli.__main__:run"
        ]
    }
)
