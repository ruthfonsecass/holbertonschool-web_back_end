#!/usr/bin/env python3
"""
function with sum_list type annotation
that receives a list of floats
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    returns their sum as a float
    """
    return sum(input_list)
