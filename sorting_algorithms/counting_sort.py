def max_min(iterable):
    max_value = None
    min_value = None

    for v in iterable:
        if max_value is None:
            max_value = v

        if min_value is None:
            min_value = v

        if v < min_value:
            min_value = v

        if v > max_value:
            max_value = v

    return min_value, max_value


def sort(iterable):
    """
    This algorithm generates an auxiliary array of counts of the numbers
    inside this iterable.

    In order to work, it must know the maximum value of the array. Since we
    don't know it, for this algorithm we will first get the maximum value
    and then perform the algorithm. Therefore we will have an extra O(n)
    operation.

    Also note that this kind of algorithm only works with integers, not with float.

    Complexity: O(n + k),
    Where k is the range of values inside the iterable (max - min)

    :param iterable:
    :return:
    """
    min_value, max_value = max_min(iterable)
    k = max_value - min_value
    if (k) > 1e8:
        raise OverflowError(
            f"Provided Array has a range of numbers too big ({k}). It will "
            f"probably crash your system memory or take too long."
        )
    # Generate an array of length being the range of integer values between
    # min and max value.
    # Negative numbers will make the array bigger, so index 0 would mean the
    # lowest negative number.
    counter = [0] * (k + 1)

    for i, v in enumerate(iterable):
        # If negative numbers, ex: -100 and min = -110 => -100 - (-110) = 10
        counter[v - min_value] += 1

    P = 0
    for i in range((max_value - min_value) + 1):
        for j in range(counter[i]):
            # Append the value to the iterable, accounting for the minimum
            # value we have removed when counting.
            iterable[P] = i + min_value
            P += 1

    return iterable
