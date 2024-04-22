def main():
    S = input()
    N = len(S)
    ans = [0] * N
    grids = []
    i = 0
    while i < N:
        j = i + 1
        counter = 1
        while j < N and S[j] == S[j - 1]:
            counter += 1
            j += 1
        grids.append((S[i], counter))
        i = j
    cursor = 0
    for i in range(len(grids)):
        if grids[i][0] == "R":
            cursor += grids[i][1] - 1
            if grids[i][1] % 2 == 0:
                tmp = grids[i][1] // 2
                ans[cursor] += tmp
                ans[cursor + 1] += tmp
            else:
                tmp = grids[i][1] // 2
                ans[cursor] += tmp + 1
                ans[cursor + 1] += tmp
            cursor += 1
        else:
            cursor += grids[i][1]
    cursor = N - 1
    for i in range(len(grids)):
        j = len(grids) - i - 1
        if grids[j][0] == "L":
            cursor -= grids[j][1] - 1
            if grids[j][1] % 2 == 0:
                tmp = grids[j][1] // 2
                ans[cursor] += tmp
                ans[cursor - 1] += tmp
            else:
                tmp = grids[j][1] // 2
                ans[cursor] += tmp + 1
                ans[cursor - 1] += tmp
            cursor -= 1
        else:
            cursor -= grids[j][1]

    print(*ans)


if __name__ == "__main__":
    main()
