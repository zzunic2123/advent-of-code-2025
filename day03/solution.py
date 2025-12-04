from pathlib import Path
from functools import cache

def solve(input_data: str):
    lines = input_data.splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def part1(lines):
    ans = 0

    for bank in lines:
        max1, max2 = float('-inf'), float('-inf')

        for i, battery in enumerate(bank):
            bat_int = int(battery)
            if bat_int > max1 and i != len(bank) - 1:
                max1 = bat_int
                max2 = float('-inf')
            elif bat_int > max2:
                max2 = bat_int

        ans += (max1 * 10 + max2)

    return ans

def part2(lines):
    # find 12 largest in right order
    ans = 0

    for bank in lines:
        ans += find(bank)

    return  ans

def find(bank):
    n = len(bank)

    @cache
    def dp(i,curr):
        if i == -1:
            return 0

        if curr > 11:
            return 0

        ans = dp(i-1, curr)

        ans = max(ans, int(bank[i]) * (10 ** curr) + dp(i-1, curr+1))
        return ans

    res = dp(n-1, 0)
    return  res

def read_input(default_path: str = "input.txt") -> str:

    # fallback: read local file
    data = []
    file_path = Path(default_path)
    if file_path.exists():
        return file_path.read_text().rstrip("\n")

    raise FileNotFoundError(f"No stdin data and file not found: {default_path}")
if __name__ == "__main__":
    input_data = read_input("input.txt")

    solve(input_data)