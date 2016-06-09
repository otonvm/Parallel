# -*- coding: utf-8 -*-

import pytest
from parallel.arguments import Arguments


def test_init():
    Arguments()

def test_init_with_list():
    Arguments([1,2,3])

def test_init_with_random():
    with pytest.raises(TypeError):
        Arguments("sometext")
