def _merge(iterable1, iterable2):
    """
    Merge two slices into a single ordered one.

    Complexity: O(n),
    Where n = len(iterable1) + len(iterable2)

    :param iterable1:
    :param iterable2:
    :return:
    """
    if not iterable1:
        return iterable2

    if not iterable2:
        return iterable1

    # Now, we iterate both. Since each iterable is already ordered
    # We only need to compare each position and append in the correct order
    n1 = len(iterable1)
    n2 = len(iterable2)

    # Pre-allocate the list to be less expensive than appending
    result = [0] * (n1 + n2)
    i1 = i2 = 0

    for i in range(n1 + n2):
        if i1 >= n1:
            result[i] = iterable2[i2]
            i2 += 1
            continue

        elif i2 >= n2:
            result[i] = iterable1[i1]
            i1 += 1
            continue

        if i2 >= n2 or iterable1[i1] <= iterable2[i2]:
            result[i] = iterable1[i1]
            i1 += 1
        else:
            result[i] = iterable2[i2]
            i2 += 1

    return result


def index_split(iterable, start, stop):
    """
    Splits the iterable starting and ending indexes in half until a single
    value remains from the [start, stop] range.

    We try to use this approach instead of splitting the iterable itself
    to see if it has some calculation cost.

    Edit:
        There was actually no visible improvement using this approach for
        high sized lists.


    :param iterable:
    :param start:
    :param stop:
    :return:
    """
    if stop - start == 1:
        return [iterable[start]]

    half_point = (stop - start) // 2

    left_half = index_split(iterable, start, start + half_point)
    right_half = index_split(iterable, start + half_point, stop)

    return _merge(left_half, right_half)


def iterable_split(iterable):
    """
    Split an iterable multiple times in half until a single element remains,
    returning it.
    Then for each half pair, merge them with a simple sorting algorithm of
    two sorted lists

    Each iteration turns out to be complexity O(n) = (2 * O(half_idx)
    But as n is divided in half at each iteration it becomes O(log(n))

    Time Complexity T(n) = 2 * T(n/2) + O(n) = O(n*log(n))
    """
    n = len(iterable)
    if n == 1:
        return iterable

    # # Divide it in two again
    half_idx = n // 2

    # Complexity O(half_idx)
    half1 = iterable_split(iterable[:half_idx])

    # Complexity O(half_idx)
    half2 = iterable_split(iterable[half_idx:])

    # Complexity O(n)
    return _merge(half1, half2)


def sort(iterable):
    """
    Perform the Merge Sort algorithm

    It aims to split the data multiple times until the numbers are
    naturally ordered due to them being a single value

    :param iterable:
    :return:
    """


    n = len(iterable)

    if n == 1:
        return iterable

    # return index_split(iterable, 0, n)
    return iterable_split(iterable)