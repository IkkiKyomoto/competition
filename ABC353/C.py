N = int(input())
A = list(map(int, input().split()))
A.sort()
S = sum(A)
count = 0
left = 0
right = N - 1
r = N
for i in range(N):
  r = max(r, i + 1)
  while r - 1 > i and A[r - 1] + A[i] >= 10 ** 8:
    r -= 1
  count += N - r
print(S * (N - 1) - (10 ** 8) * count)