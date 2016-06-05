# -*- coding: utf-8 -*-

"""Usage:
    test_doc -h | --help
    test_doc -V | --version
    test_doc -v | --verbose
    test_doc -d | --debug
    test_doc [options] <command> [<arguments>...]

Options:
    -h --help     Show this screen.
    -V --version  Show program version.
    -v --verbose  Show additional information.
    -d --debug    Show debugging messages.

Arguments:
    <command>     Command to execute.
                  Must be an executable or a script, present in your PATH or
                  a full path to the executable.
    <arguments>   Optional argument for the command.
                  The following replacement strings are available:
                  {fullpath}    full path to the file
                  {filename}    file name with extension
                  {parentpath}  full path to the file parent folder
                  {basename}    file name without extension
                  {ext}         file extension

"""

import os
import docopt
import pathlib

__version__ = 0.1


class ExecutableNotFoundError(Exception):
    pass


class Command:
    def __init__(self, path=None):
        self._setup_path(path)
        self._check_path(path)

    def _setup_path(self, original_value):
        try:
            self._path = pathlib.Path(original_value)
        except TypeError:
            self._path = None

    def _check_path(self, original_value):
        if self._path and not self._path.is_file():
            raise ExecutableNotFoundError("Cannot find {}".format(original_value))

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._setup_path(value)
        self._check_path(value)


def main():
    args = docopt.docopt(__doc__, version=__version__, options_first=True)


if __name__ == "__main__":
    main()
