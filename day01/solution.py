from pathlib import Path

DIAL_LEN = 100

def solve(input_data: str):
    lines = input_data.splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def part1(lines):
    curr_point = 50
    ans = 0

    for rotation in lines:
        direction = rotation[0]
        rotation = int(''.join(rotation[1:]))
        if direction == 'L':
            rotation = -rotation
        curr_point += rotation
        curr_point %= DIAL_LEN
        if curr_point == 0:
            ans += 1
        #print(direction + " " + str(rotation) + "  solution: " + str(curr_point))

    return ans

def part2(lines):
    curr_point = 50
    ans = 0

    for rotation in lines:
        direction = rotation[0]
        steps = int(''.join(rotation[1:]))

        if direction == 'L':
            steps = -steps

        k = steps

        if k != 0:
            forward = k > 0
            dist = abs(k)

            if forward:
                first = (DIAL_LEN - curr_point) % DIAL_LEN
            else:
                first = curr_point % DIAL_LEN

            if first == 0:
                first = DIAL_LEN

            if dist >= first:
                hits = 1 + (dist - first) // DIAL_LEN
                ans += hits

        curr_point = (curr_point + steps) % DIAL_LEN


    return ans

def read_input(default_path: str = "input.txt") -> str:
    """Read from stdin if available, otherwise from the given file path."""

    # fallback: read local file
    file_path = Path(default_path)
    if file_path.exists():
        return file_path.read_text().rstrip("\n")

    raise FileNotFoundError(f"No stdin data and file not found: {default_path}")

if __name__ == "__main__":
    input_data = read_input("input.txt")
    solve(input_data)
