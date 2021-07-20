#!/usr/bin/env python3

import functools #Needed to get .abc in collections to work
import collections
"""
    collections.abc.Iterable was the only method I could find that 
    would reliably handle 3D nested (integer only) lists.  The 
    collections library changed around v3.3+ such that the
    .abc.Iterable() method lives somewhere else, likely incorporated
    into another existing library, because it works with the 'functions'
    import despite not being called anywhere.
"""

l = [[1, 2, 3], [4, 5, [6]], [7], [8, 9]]
l2 = [[1,2,[3]],4]


def deep_flatten(l):
    for elem in l:
        # checks if elem is iterable, and excludes strings and bytes
        if isinstance(elem, collections.abc.Iterable) and not isinstance(elem, (str, bytes)):
            yield from deep_flatten(elem)
        else:
            yield elem


if __name__ == '__main__':
    print(list(deep_flatten(l)))
    print(list(deep_flatten(l2)))
