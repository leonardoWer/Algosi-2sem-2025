def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])  # Берем минимум, чтобы не выйти за границы
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def main():
    with open("input.txt", "r") as file:
        s = file.readline().strip()

    z = z_function(s)

    with open("output.txt", "w") as file:
        file.write(" ".join(map(str, z[1:])) + "\n")


if __name__ == "__main__":
    main()