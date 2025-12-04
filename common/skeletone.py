from pathlib import Path


def solve(input_data: str):
    lines = input_data.splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def part1(lines):

    return None

def part2(lines):

   return None

def read_input(default_path: str = "input.txt") -> str:

    # fallback: read local file
    file_path = Path(default_path)
    if file_path.exists():
        return file_path.read_text().rstrip("\n")

    raise FileNotFoundError(f"No stdin data and file not found: {default_path}")
if __name__ == "__main__":
    input_data = read_input("input.txt")
    solve(input_data)