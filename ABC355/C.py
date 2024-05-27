N, T = map(int, input().split())
A = list(map(int, input().split()))
row = [0 for _ in range(N)]
column = [0 for _ in range(N)]
diag = [0 for _ in range(2)]
flag = False
ans = -1
for i in range(T):
  x = (A[i] - 1) // N
  y = (A[i] - 1) % N
  if x < N:
    row[x] += 1
    column[y] += 1
    if x == y:
      diag[0] += 1
    if x + y == N - 1:
      diag[1] += 1
    if row[x] == N or column[y] == N or diag[0] == N or diag[1] == N:
      flag = True
      ans = i + 1
      break
print(ans)
      