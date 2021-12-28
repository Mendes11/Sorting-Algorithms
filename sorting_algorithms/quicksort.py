
def lomuto_partition(iterable, initial_idx, partition_length):
    # Here, we assume pivot to always be the last element, therefore
    # partition_length - 1
    pivot_idx = partition_length - 1
    pivot = iterable[pivot_idx]

    # Here, i points to the final element of the slice (partition) that
    # contains the values that are lower than pivot.
    # It starts out of the partition, since we assume first that all values
    # are higher than pivot.
    i = initial_idx - 1

    for j in range(initial_idx, partition_length - 1):
        # Every time we find a value that is lower than pivot, we need to
        # move our pointer "i" to the next position where we will place this
        # value that is lower.

        # Note that we start out of the slice, so the first value will be
        # put at position 0.

        if iterable[j] <= pivot:
            i += 1
            # Swap current value to where i points
            iterable[i], iterable[j] = iterable[j], iterable[i]

    # Now, all values bellow pivot are at positions j, with 0 <= j <= i
    # Since this algorithm considers that the only correctly ordered value
    # is the pivot, we will put it on its correct place.
    # That is, after all values that are bellow it! Since i points to the
    # last position of the value that is under it, we move the cursor by one
    # and insert the pivot there! This ensures that the pivot is in the
    # correct place!

    i += 1
    iterable[i], iterable[pivot_idx] = iterable[pivot_idx], iterable[i]

    return i


def quick_sort(iterable, initial_idx=0, partition_length=None):
    partition_length = partition_length if partition_length is not None else len(iterable)
    if initial_idx < partition_length:
        partition = lomuto_partition(iterable, initial_idx, partition_length)
        quick_sort(iterable, initial_idx, partition)
        quick_sort(iterable, partition + 1, partition_length)

    return iterable


def sort(iterable):
    return quick_sort(iterable)
