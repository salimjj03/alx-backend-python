#!/usr/bin/env python3
""" this model takes a float multiplier as
argument and returns a function that multiplies
a float by multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ this model takes a float multiplier as
    argument and returns a function that multiplies
    a float by multiplier. """

    def mult(n: float) -> float:
        """ multiplies a float by multiplier. """

        return n * multiplier
    return mult
