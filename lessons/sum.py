"""This sums a list."""

def sum_old(xs: list[float]) -> float: 
    """return sum of elements in a list"""
    sum_total = 0.0 
    for value in xs: 
        sum_total += value  
    return sum_total


def sum(xs: list[float]) -> float: 
    """return sum of elements in a list"""
    sum_total = 0.0 
    idx = 0
    for idx in range(0,len(xs),1): 
        sum_total += xs[idx]
    return sum_total