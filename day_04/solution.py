import time
from collections import defaultdict


def process_input(path: str) -> list[list[str]]:
    with open(path) as fp:
        output = []
        while line := fp.readline():
            output.append(list(line))

        return output


def main():
    grid = process_input("./puzzle.txt")

    start_time = time.perf_counter()
    result = count_xmas(grid)
    end_time = time.perf_counter()

    print(f"Part 1: {result}")
    print("Time: {}".format(end_time - start_time))

    print("----")

    start_time = time.perf_counter()
    result = count_x_mas(grid)
    end_time = time.perf_counter()

    print(f"Part 2: {result}")
    print("Time: {}".format(end_time - start_time))


def count_x_mas(grid: list[list[str]]) -> int:
    x_counter: dict[tuple[int, int], int] = defaultdict(int)

    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            count_x_mas_recurse(grid, row, col, "MAS", 0, -1, -1, x_counter)
            count_x_mas_recurse(grid, row, col, "MAS", 0, -1, 1, x_counter)
            count_x_mas_recurse(grid, row, col, "MAS", 0, 1, -1, x_counter)
            count_x_mas_recurse(grid, row, col, "MAS", 0, 1, 1, x_counter)

    sum = 0

    for v in x_counter.values():
        if v == 2:
            sum += 1

    return sum


def count_x_mas_recurse(
    grid: list[list[str]],
    row: int,
    col: int,
    word: str,
    letter_idx: int,
    vertical: int,
    horizontal: int,
    cache: dict[tuple[int, int], int],
):
    if (
        row < 0
        or row >= len(grid)
        or col < 0
        or col >= len(grid[row])
        or letter_idx >= len(word)
        or grid[row][col] != word[letter_idx]
    ):
        return

    if letter_idx == len(word) - 1:
        cache[row - ((len(word) // 2) * vertical), col - ((len(word) // 2) * horizontal)] += 1
        return

    count_x_mas_recurse(grid, row + (1 * vertical), col + (1 * horizontal), word, letter_idx + 1, vertical, horizontal, cache)


def count_xmas(grid: list[list[str]]) -> int:
    sum = 0

    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, 0, 1)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, 0, -1)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, 1, 0)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, -1, 0)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, 1, 1)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, 1, -1)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, -1, 1)
            sum += count_xmas_recurse(grid, row, col, "XMAS", 0, -1, -1)

    return sum


def count_xmas_recurse(
    grid: list[list[str]], row: int, col: int, word: str, letter_idx: int, vertical: int, horizontal: int
) -> int:
    if (
        row < 0
        or row >= len(grid)
        or col < 0
        or col >= len(grid[row])
        or letter_idx >= len(word)
        or grid[row][col] != word[letter_idx]
    ):
        return 0

    if letter_idx == len(word) - 1:
        return 1

    return count_xmas_recurse(grid, row + (1 * vertical), col + (1 * horizontal), word, letter_idx + 1, vertical, horizontal)


if __name__ == "__main__":
    main()
