N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i - 1]
pos = 0
while pos + K < N + 1:
    print(S[pos + K] - S[pos])
    pos += 1
