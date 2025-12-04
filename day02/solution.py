from pathlib import Path

def solve(ranges):
    print(ranges)

    print("Part 1:", part1(ranges))
    print("Part 2:", part2(ranges))

def find_start(start):
    if len(start) % 2 == 0:
        return start

    return str(10 ** len(start))

def is_invalid_id(start):
    start = str(start)
    return start[:len(start)//2] == start[len(start)//2:]

def invalid_ids_sum(start, end):
    start = find_start(start)

    cnt = 0
    start = int(start)
    end = int(end)

    while start <= end:
        if len(str(start)) % 2 != 0:
            start = 10 ** len(str(start))

        if is_invalid_id(start):
            cnt+=start
        start+=1

    return cnt

def part1(ranges):

    ans = 0

    for range in ranges:
        ans += invalid_ids_sum(range[0], range[1])

    return ans

def is_invalid_id_seq(start):
    start = str(start)
    # 12131213
    n = len(start)

    for c in range(1, n//2 + 1):
        if n % c != 0:
            continue

        chunk = start[:c]

        if chunk * (n // c) == start:
            return True

    return False


def invalid_ids_seq(start, end):
    #start = find_start(start)

    cnt = 0
    start = int(start)
    end = int(end)

    while start <= end:

        if is_invalid_id_seq(start):
            cnt+=start
        start+=1

    return cnt

def part2(ranges):
    ans = 0

    for range in ranges:
        ans += invalid_ids_seq(range[0], range[1])

    return ans

def read_input(default_path: str = "input.txt") -> str:
    file_path = Path(default_path)
    if not file_path.exists():
        raise FileNotFoundError(f"No file found: {default_path}")

    text = file_path.read_text().strip()

    ranges = []
    for part in text.split(","):
        start, end = part.split("-")
        ranges.append((start, end))

    return ranges

if __name__ == "__main__":
    input_data = read_input("input.txt")
    solve(input_data)