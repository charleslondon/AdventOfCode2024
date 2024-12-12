import time


def process_input(path: str) -> list[int]:
    with open("./puzzle.txt") as fp:
        return list(map(int, fp.readline().split()))


def main():
    stones = process_input("./puzzle.txt")

    stones_part1 = [(x, 25) for x in stones]
    start_time = time.perf_counter()
    result = calc_sum({}, stones_part1)
    end_time = time.perf_counter()

    print(f"Part 1: {result}")
    print("Time: {}".format(end_time - start_time))

    print("----")

    stones_part2 = [(x, 75) for x in stones]
    start_time = time.perf_counter()
    result = calc_sum({}, stones_part2)
    end_time = time.perf_counter()

    print(f"Part 2: {result}")
    print("Time: {}".format(end_time - start_time))


def calc_sum(cache: dict[(int, int), int], stones: list[(int, int)]) -> int:
    counter = 0

    while stones:
        (stone, iteration) = stones.pop()

        if iteration == 0:
            counter += 1
        else:
            if cache.get((stone, iteration)) is None:
                cache[(stone, iteration)] = calc_sum(cache, blink(stone, iteration - 1))
            counter += cache[(stone, iteration)]

    return counter


def blink(stone: int, iteration: int) -> list[(int, int)]:
    if stone == 0:
        return [(1, iteration)]

    stone_str = str(stone)

    if (stone_len := len(stone_str)) % 2 == 0:
        half = stone_len // 2
        (left, right) = stone_str[:half], stone_str[half:]
        return [(int(left), iteration), (int(right), iteration)]

    return [(int(stone) * 2024, iteration)]


if __name__ == "__main__":
    main()
