import random
from timeit import repeat

from matplotlib import pyplot as plt


def run_sorting_algorithm(algorithm, iterable):
    setup = f"""from sorting_algorithms import {algorithm}"""
    stmt = f"{algorithm}.sort({iterable})"
    times = repeat(stmt=stmt, setup=setup, repeat=3, number=10)


    return sum(times) / len(times)


def _print_table(columns, indexes, rows):
    columns = "\t\t".join(columns)
    print(f"\t{columns}")
    for idx, row in zip(indexes, rows):
        row_str = "\t".join(map(str, row))
        print(f"{idx}\t{row_str}")


def _plot_performances(algorithms, sizes, times):
    plt.plot(sizes, times)
    plt.legend(algorithms)
    plt.title("Sorting Algorithms Complexity")
    plt.show()


if __name__ == '__main__':
    algorithms = [
        # "selection_sort",
        "counting_sort",
        "merge_sort",
        "quicksort",
        "python_sort"
    ]
    max_size = 1e2
    sizes = range(10, int(max_size), int((max_size - 10) // 10))
    performances = []

    for size in sizes:
        iterable = [
            random.randint(int(-1e3), int(1e3))
            for _ in range(int(size))
        ]
        size_avg_times = []
        for alg in algorithms:
            avg_time = run_sorting_algorithm(alg, iterable)
            size_avg_times.append(avg_time)
        performances.append(size_avg_times)

    _print_table(algorithms, sizes, performances)
    _plot_performances(algorithms, sizes, performances)