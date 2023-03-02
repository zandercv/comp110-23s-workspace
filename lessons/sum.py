"""This sums a list."""

def sum(xs: list[float]) -> float: 
    """return sum of elements in a list"""
    sum_total = 0.0 
    for value in xs: 
        sum_total += value  
    return sum_total


