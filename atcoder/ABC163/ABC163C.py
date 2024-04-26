N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(len(A)):
    G[A[i] - 1].append(i + 1)

for i in range(N):
    print(len(G[i]))
