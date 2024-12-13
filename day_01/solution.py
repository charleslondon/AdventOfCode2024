import time
from collections import Counter


def process_input(path: str) -> (list[int], list[int]):
    with open(path) as fp:
        left, right = [], []

        while line := fp.readline():
            _l, _r = map(int, line.split())
            left.append(_l)
            right.append(_r)

        return left, right


def main():
    left, right = process_input("./puzzle.txt")

    start_time = time.perf_counter()
    result = calc_difference(left, right)
    end_time = time.perf_counter()

    print(f"Part 1: {result}")
    print("Time: {}".format(end_time - start_time))

    print("----")

    start_time = time.perf_counter()
    result = calc_similarity(left, right)
    end_time = time.perf_counter()

    print(f"Part 2: {result}")
    print("Time: {}".format(end_time - start_time))


def calc_difference(left: list[int], right: list[int]) -> int:
    count = 0

    left.sort()
    right.sort()

    for _l, _r in zip(left, right):
        count += abs(_l - _r)

    return count


def calc_similarity(left: list[int], right: list[int]) -> int:
    count = 0

    freqs = Counter(right)
    for _l in left:
        count += _l * freqs[_l]

    return count


if __name__ == "__main__":
    main()
