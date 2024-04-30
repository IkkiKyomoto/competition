N = int(input())
S = [[0 for i in range(N + 1)] for i in range(2)]
for i in range(1, N + 1):
    c, p = map(int, input().split())
    c = (c + 1) % 2
    S[c][i] = S[c][i - 1] + p
    c = (c + 1) % 2
    S[c][i] = S[c][i - 1]

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(*[e[r] - e[l - 1] for e in S])
