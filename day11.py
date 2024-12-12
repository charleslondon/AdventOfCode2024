import time


def main():
    iters = 75
    stones = [92, 0, 286041, 8034, 34394, 795, 8, 2051489]
    stones = [(x, iters) for x in stones]

    start_time = time.perf_counter()
    result = calc_sum({}, stones)
    end_time = time.perf_counter()

    print(result)
    print(end_time - start_time)


def calc_sum(cache: dict[(int, int), int], stones: list[(int, int)]) -> int:
    counter = 0

    while stones:
        (stone, iteration) = stones.pop()

        if iteration == 0:
            counter += 1
        else:
            if cache.get((stone, iteration)) is None:
                cache[(stone, iteration)] = calc_sum(cache, blink(stone, iteration))
            counter += cache[(stone, iteration)]

    return counter


def blink(stone: int, iteration: int) -> list[(int, int)]:
    if stone == 0:
        return [(1, iteration - 1)]

    stone_str = str(stone)

    if (stone_len := len(stone_str)) % 2 == 0:
        half = stone_len // 2
        (left, right) = stone_str[:half], stone_str[half:]
        return [(int(left), iteration - 1), (int(right), iteration - 1)]

    return [(int(stone) * 2024, iteration - 1)]


if __name__ == "__main__":
    main()
