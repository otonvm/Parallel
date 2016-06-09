# -*- coding: utf-8 -*-

import pathlib
from .execptions import ExecutableNotFoundError


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
