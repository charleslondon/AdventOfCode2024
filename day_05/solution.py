import time
from collections import defaultdict


def process_input(path1: str, path2: str) -> (list[tuple[int, int]], list[list[int]]):
    rules = []
    with open(path1) as fp:
        while line := fp.readline():
            rules.append(tuple([int(x) for x in line.strip().split("|")]))

    updates = []
    with open(path2) as fp:
        while line := fp.readline():
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def main():
    rules, updates = process_input("./puzzle1.txt", "./puzzle2.txt")

    start_time = time.perf_counter()
    result = sum_safe_medians(rules, updates)
    end_time = time.perf_counter()

    print(f"Part 1: {result}")
    print("Time: {}".format(end_time - start_time))

    print("----")

    start_time = time.perf_counter()
    # result = sum_corrected_unsafe_medians(rules, updates)
    end_time = time.perf_counter()

    print(f"Part 2: {result}")
    print("Time: {}".format(end_time - start_time))


def sum_safe_medians(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    rule_mapping = defaultdict(set)

    for rule in rules:
        rule_mapping[rule[0]].add(rule[1])

    safe_updates = []

    for update in updates:
        seen = set()
        error = False
        for page in update:
            if seen.intersection(rule_mapping[page]):
                error = True
                break
            else:
                seen.add(page)
        if not error:
            safe_updates.append(update)

    sum = 0

    for update in safe_updates:
        sum += update[len(update) // 2]

    return sum


if __name__ == "__main__":
    main()
