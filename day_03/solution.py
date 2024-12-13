import re
import time


def process_input(path: str) -> str:
    with open(path) as fp:
        return fp.read()


def main():
    data = process_input("./puzzle.txt")

    start_time = time.perf_counter()
    result = sum_instructions(data)
    end_time = time.perf_counter()

    print(f"Part 1: {result}")
    print("Time: {}".format(end_time - start_time))

    print("----")

    start_time = time.perf_counter()
    result = sum_advanced_instructions(data)
    end_time = time.perf_counter()

    print(f"Part 2: {result}")
    print("Time: {}".format(end_time - start_time))


def sum_instructions(data: str) -> int:
    pattern = r"mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)"

    instructions = re.findall(pattern, data)
    instructions = [x[4:-1] for x in instructions]
    instructions = [list(map(int, x.split(","))) for x in instructions]
    instructions = [x[0] * x[1] for x in instructions]

    return sum(instructions)


def sum_advanced_instructions(data: str) -> int:
    negations = data.split("don't()")

    sum = sum_instructions(negations[0])

    for datum in negations[1:]:
        split = datum.split("do()", 1)

        if len(split) == 2:
            sum += sum_instructions(split[1])

    return sum


if __name__ == "__main__":
    main()
