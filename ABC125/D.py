N = int(input())
A = list(map(int, input().split()))
num_minus = sum(v < 0 for v in A)
ans = 0
if num_minus % 2 == 0:
  ans = sum(map(abs, A))
else:
  ans = sum(map(abs, A)) - min(map(abs, A)) * 2
print(ans)