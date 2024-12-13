import time


def process_input(path: str) -> list[list[int]]:
    with open(path) as fp:
        reports = []

        while levels := fp.readline():
            reports.append(list(map(int, levels.split())))

        return reports


def main():
    reports = process_input("./puzzle.txt")

    start_time = time.perf_counter()
    result = calc_safe_reports(reports, 0)
    end_time = time.perf_counter()

    print(f"Part 1: {result}")
    print("Time: {}".format(end_time - start_time))

    print("----")

    start_time = time.perf_counter()
    result = calc_safe_reports(reports, 1)
    end_time = time.perf_counter()

    print(f"Part 2: {result}")
    print("Time: {}".format(end_time - start_time))


def calc_safe_reports(reports: list[list[int]], tolerance: int) -> int:
    count = 0

    for report in reports:
        if valid(report, tolerance):
            count += 1

    return count


def valid(report: list[int], tolerance: int) -> bool:
    if len(report) < 2:
        return True
    if report[0] == report[1]:
        return False

    sign = 1
    if report[0] > report[1]:
        sign = -1

    for idx in range(1, len(report)):
        prev = report[idx - 1]
        curr = report[idx]
        delta = (curr - prev) * sign
        if delta < 1 or delta > 3:
            if tolerance == 0:
                return False
            tolerance -= 1

    return True


if __name__ == "__main__":
    main()
