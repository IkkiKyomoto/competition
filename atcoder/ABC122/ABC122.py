N, Q = map(int, input().split())
inp = input()
S = [0] * (N + 1)
for i in range(1, N + 1):
    if inp[i - 2 : i] == "AC":
        S[i] = S[i - 1] + 1
    else:
        S[i] = S[i - 1]
for i in range(Q):
    l, r = map(int, input().split())
    print(S[r] - S[l])
