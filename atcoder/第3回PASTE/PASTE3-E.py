N, M, Q = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
c = [None] + list(map(int, input().split()))
for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        print(c[s[1]])
        for e in G[s[1]]:
            c[e] = c[s[1]]
    elif s[0] == 2:
        print(c[s[1]])
        c[s[1]] = s[2]
