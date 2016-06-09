# -*- coding: utf-8 -*-


class Arguments:
    def __init__(self, list_of_arguments=None):
        if list_of_arguments is not None:
            if not isinstance(list_of_arguments, list):
                raise TypeError("Must provide a list of arguments!")
