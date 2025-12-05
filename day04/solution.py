from pathlib import Path


def solve(input_data: str):
    lines = input_data.splitlines()
    print(lines)

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def part1(lines):

    def valid(row,col):
        return 0 <= row < m and 0 <= col < n and lines[row][col] == "@"
    m = len(lines)
    n = len(lines[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1),(-1,1)]

    ans = 0
    for i in range(m):
        for j in range(n):
            if lines[i][j] != "@":
                continue
            cnt = 0
            for dx,dy in directions:
                n_x , n_y = i + dx, j + dy
                if valid(n_x, n_y):
                    cnt+=1
            if cnt < 4:
                ans+=1

    return ans

def part2(lines):
    def valid(row,col):
        return 0 <= row < m and 0 <= col < n and lines[row][col] == "@"
    m = len(lines)
    n = len(lines[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1),(-1,1)]

    for i in range(m):
        lines[i] = list(lines[i])


    res = 0
    ans = 0
    while ans != -1:
        ans = 0

        for i in range(m):
            for j in range(n):
                if lines[i][j] != "@":
                    continue
                cnt = 0
                for dx,dy in directions:
                    n_x , n_y = i + dx, j + dy
                    if valid(n_x, n_y):
                        cnt+=1
                if cnt < 4:
                    lines[i][j] = "."
                    ans+=1

        res += ans
        if ans == 0:
            ans = -1
    return res

def read_input(default_path: str = "input.txt") -> str:

    # fallback: read local file
    file_path = Path(default_path)
    if file_path.exists():
        return file_path.read_text().rstrip("\n")

    raise FileNotFoundError(f"No stdin data and file not found: {default_path}")
if __name__ == "__main__":
    input_data = read_input("input.txt")
    solve(input_data)