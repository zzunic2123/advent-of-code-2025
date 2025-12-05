from pathlib import Path

def solve(ranges, ids):
    print("Part 1:", part1(ranges, ids))
    print("Part 2:", part2(ranges, ids))


def part1(ranges, ids):
    #brute force - add everything to a set

    def b_search(target):
        left = 0
        right = len(merged_ranges) - 1

        while left <= right:
            mid = (left+right) // 2

            a,b = merged_ranges[mid]

            if a <= target <= b:
                return True
            elif target > b:
                left = mid+1
            else:
                right = mid-1

        return False

    merged_ranges = merge_intervals(ranges)

    # binary search
    fresh = 0

    for id in ids:
        if b_search(id):
            fresh+=1

    return fresh

def merge_intervals(ranges):
    ranges.sort(key=lambda x: x[0])
    # merge intervals
    merged_ranges = [ranges[0]]

    for i in range(1, len(ranges)):
        last = merged_ranges[-1]
        curr = ranges[i]

        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            merged_ranges.append(curr)

    return merged_ranges


def part2(ranges, ids):

    merged_ranges = merge_intervals(ranges)

    cnt = 0

    for a,b in merged_ranges:
        cnt += (b-a + 1)

    return cnt


def read_input(path="input.txt"):

    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    text = file.read_text().strip("\n").splitlines()

    ranges = []
    ids = []

    i = 0

    # Read ranges until blank line
    while i < len(text) and text[i].strip() != "":
        start, end = text[i].split("-")
        ranges.append([int(start), int(end)])
        i += 1

    # Skip the blank line
    while i < len(text) and text[i].strip() == "":
        i += 1

    # Read the ingredient IDs
    while i < len(text):
        ids.append(int(text[i]))
        i += 1

    return ranges, ids


if __name__ == "__main__":
    ranges, ids = read_input("input.txt")
    solve(ranges, ids)
