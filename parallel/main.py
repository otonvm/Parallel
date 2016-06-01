# -*- coding: utf-8 -*-

import os
import argparse

__version__ = 0.1


class NewlineFormatter(argparse.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _split_lines(self, text, width):
        if text.startswith("R>"):
            return text[2:].splitlines()
        return super()._split_lines(text, width)


class Options:
    verbose = None
    jobs = None
    command = None
    arguments = None


def parse_options():
    parser = argparse.ArgumentParser(formatter_class=NewlineFormatter,
                                     description="Process files in parallel.")

    parser.add_argument("-V", "--version", action="version",
                        version="{} v{}".format("%(prog)s", __version__))
    parser.add_argument("-v", "--verbose", action="count",
                        help=("R>print additional information\n"
                              "Specify multiple times to enable debugging messages."))
    parser.add_argument("-j", "--jobs", type=int, metavar="n",
                        help=("R>how many jobs to spawn concurrently\n"
                              "If not specified defaults to number of "
                              "CPU cores present (current: {}).".format(os.cpu_count())))
    parser.add_argument("command",
                        help=("R>command to execute\n"
                              "Must be an executable or a script.\n"
                              "If it's not in your PATH it must be a full path."))
    parser.add_argument("arguments", nargs=argparse.REMAINDER, default=None, metavar="[arguments]",
                        help=("R>optional arguments for the command\n"
                              "The following replacement strings are available:\n"
                              "{fullpath}    full path to the file\n"
                              "{basename}    file name without extension\n"
                              "{ext}         only file extension\n"
                              "{name}        {basename}+{ext}"))

    parser.parse_args("-h".split(), namespace=Options)


def main():
    parse_options()


if __name__ == "__main__":
    main()
