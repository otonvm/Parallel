# -*- coding: utf-8 -*-

import pytest
from parallel.command import Command
from parallel.execptions import ExecutableNotFoundError


def test_init():
    Command()

def test_init_with_something():
    with pytest.raises(ExecutableNotFoundError):
        Command("sometext")

def test_init_with_valid():
    Command("/bin/rm")

def test_path_property_valid():
    Command().path = "/bin/rm"

def test_path_property_invalid():
    with pytest.raises(ExecutableNotFoundError):
        Command().path = "sometext"
