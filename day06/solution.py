from pathlib import Path


def read_input(path="input.txt"):
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    rows = file.read_text().splitlines()

    matrix = []

    for line in rows:
        tokens = line.split()
        matrix.append(tokens)

    return matrix


def solve(lines):
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


def part1(lines):
    m = len(lines)
    n = len(lines[0])

    ans = 0

    for i in range(n):
        operator = lines[m-1][i]
        col_result = 0
        for j in range(m-2,-1,-1):
            curr = lines[j][i]
            if operator == '+':
                col_result += int(curr)
            else:
                if col_result == 0:
                    col_result = 1
                col_result *= int(curr)
        ans += col_result

    return ans


def part2(lines):
    lines = read_input_matrix()
    print("=== INPUT MATRIX ===")
    for row in lines:
        print(row)
    print("====================")
    m = len(lines)
    n = len(lines[0])

    res = 0
    curr = []
    operator = None

    for i in range(n-1,-1,-1):

        number = ''
        for j in range(m):

            if j == m-1:
                if lines[j][i] not in ['*', '+']:
                    continue
                else:
                    operator = lines[j][i]
            else:
                number += lines[j][i]

        if number.strip() == '':
            continue
        if operator:
            curr.append(int(number.strip()))
            temp = 0
            if operator == '+':
                for c in curr:
                    temp += c
            else:
                temp = 1
                for c in curr:
                    temp *= c
            print(temp)
            print('/////////')
            res += temp
            operator = None
            curr = []
        else:
            print(int(number.strip()))
            curr.append(int(number.strip()))

    return res

def read_input_matrix(path="input.txt"):
    lines = Path(path).read_text().splitlines()
    width = max(len(line) for line in lines)

    # Build full character matrix (with spaces preserved)
    matrix = [list(line.ljust(width)) for line in lines]
    return matrix



if __name__ == "__main__":
    lines = read_input("input.txt")
    solve(lines)
