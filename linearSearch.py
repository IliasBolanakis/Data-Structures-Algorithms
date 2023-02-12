from typing import List, TypeVar

"""

A module for searching the k-th smallest element 
in an unsorted mutable list in linear time. 

The performance benefits lies in the selection of 
a partitioning element that with each iteration disregards 
at least a certain percentage of the array, hence making 
the algorithm more efficient (Θ(n) complexity)  

Author: Ilias Bolanakis 
"""

# used for dynamic type hinting
__T = TypeVar("__T")


def linear_search(data: List[__T], k: int) -> __T:
    """

    Finds the k-th smallest element in a list in O(n).
    Note: Mutation occurs!

    :param data: The list to search.
    :param k: The k-th smallest element to search for
    :return: the k-th smallest element of data
    """
    n = len(data)
    # base case of the algorithm
    if n <= 100:
        return sorted(data)[k-1]

    # find the median of n/5 subarrays of 5 max elements each
    medians = [sorted(data[i:i + 5])[len(data[i:i + 5]) // 2]
               for i in range(0, n, 5)]

    # calculate the median of medians
    pivot, _ = divmod(len(medians), 2)
    pivot = linear_search(medians, pivot + 1)

    # low = {data[i], data[i] < pivot}, high = {data[i], data[i] >= pivot}
    low, high = [x for x in data if x < pivot], [x for x in data if x >= pivot]

    # continue searching in the appropriate section
    return linear_search(low, k) if k <= len(low) else linear_search(high, k - len(low))
