#!/usr/bin/env python3
"""  return values with the appropriate types """

from typing import Sequence, Tuple


def element_length(lst: Sequence[str]) -> Sequence[Tuple[str, int]]:
    """
     return values with the appropriate types
    """

    return [(i, len(i)) for i in lst]
