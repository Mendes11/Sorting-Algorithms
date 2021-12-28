def sort(iterable):
    """
    Selection Sort works by iterating through the entire array and selects
    the minimal value of that array, swapping the first element with it.

    Then it repeat the same procedure, but ignoring the first element,
    which is already sorted.

    This version does not works with generators.

    Complexity: O(n²)

    :param iterable:
    :return: Sorted Iterable
    """

    for i in range(len(iterable)):
        minimum = iterable[i]
        min_index = i
        for j, v in enumerate(iterable[i:], i):
            if v < minimum:
                minimum = v
                min_index = j
        iterable[i], iterable[min_index] = iterable[min_index], iterable[i]

    return iterable
