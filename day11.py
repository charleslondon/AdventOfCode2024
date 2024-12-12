import time

def main():
    start_time = time.time()
    memo = {}
    iters = 960
    stones = [92, 0, 286041, 8034, 34394, 795, 8, 2051489]
    stones = [(x, iters) for x in stones]
    result = count_recursive(memo, stones)
    end_time = time.time()
    print(result)
    print(end_time - start_time)

def count_recursive(memo: dict[(int, int), int], stones: list[int]) -> int:
    counter = 0

    while len(stones) > 0:
        (s, i) = stones.pop()

        if (val := memo.get((s, i))) is not None:
            counter += val
        elif i == 0:
            counter += 1
        else:
            memo[(s, i)] = count_recursive(memo, calc_next(s, i))
            counter += memo[(s, i)]

    return counter

def calc_next(s: int, i: int) -> list[(int, int)]:
    if s == 0:
        return [(1, i - 1)]

    s_str = str(s)

    if (s_len := len(s_str)) % 2 == 0:
        half = s_len // 2
        (left, right) = s_str[:half], s_str[half:]
        return [(int(left), i - 1), (int(right), i - 1)]

    return [(int(s) * 2024, i - 1)]

























if __name__ == "__main__":
    main()
