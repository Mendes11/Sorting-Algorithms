import pytest

from sorting_algorithms import selection_sort
from sorting_algorithms import counting_sort
from sorting_algorithms import merge_sort
from sorting_algorithms import quicksort


@pytest.mark.parametrize(
    ["iterable", "res"],
    [
        ([5, 1, 7, 5, 9, 9, 5, 3, 10, 55, 2], [1, 2, 3, 5, 5, 5, 7, 9, 9, 10, 55]),
        ([5, 1, 7, 5, 9, -1, -10], [-10, -1, 1, 5, 5, 7, 9]),
    ]
)
def test_selection_sort(iterable, res):
    assert selection_sort.sort(iterable) == res

@pytest.mark.parametrize(
    ["iterable", "res"],
    [
        ([5, 1, 7, 5, 9, 9, 5, 3, 10, 55, 2], [1, 2, 3, 5, 5, 5, 7, 9, 9, 10, 55]),
        ([5, 1, 7, 5, 9, -1, -10], [-10, -1, 1, 5, 5, 7, 9]),
    ]
)
def test_counting_sort(iterable, res):
    assert counting_sort.sort(iterable) == res

@pytest.mark.parametrize(
    ["iterable", "res"],
    [
        ([5, 1, 7, 5, 9, 9, 5, 3, 10, 55, 2], [1, 2, 3, 5, 5, 5, 7, 9, 9, 10, 55]),
        ([5, 1, 7, 5, 9, -1, -10], [-10, -1, 1, 5, 5, 7, 9]),
    ]
)
def test_merge_sort(iterable, res):
    assert merge_sort.sort(iterable) == res


@pytest.mark.parametrize(
    ["iterable", "res"],
    [
        ([5, 1, 7, 5, 9, 9, 5, 3, 10, 55, 2], [1, 2, 3, 5, 5, 5, 7, 9, 9, 10, 55]),
        ([5, 1, 7, 5, 9, -1, -10], [-10, -1, 1, 5, 5, 7, 9]),
    ]
)
def test_quicksort(iterable, res):
    assert quicksort.sort(iterable) == res
