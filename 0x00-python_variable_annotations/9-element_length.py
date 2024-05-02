#!/usr/bin/env python3
"""  return values with the appropriate types """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence[str]]) -> List[
        Tuple[Sequence[str], int]
        ]:

    """
     return values with the appropriate types
    """

    return [(i, len(i)) for i in lst]
