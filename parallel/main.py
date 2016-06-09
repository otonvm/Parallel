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

import docopt
from .command import Command


__version__ = 0.1


def main():
    args = docopt.docopt(__doc__, version=__version__, options_first=True)


if __name__ == "__main__":
    main()
