M = 998244353

def solve(case):
  ans = 0
  a = 10 ** (case[0] - 1)
  b = 10 ** case[0] - 1
  if case[2] - case[1] == 1:

    ans = ((a + b) * (b - a + 1)) // 2
  elif case[2] - case[1] == 0:
    c = 0
    d = b - a
    ans = ((c + d) * (b - a + 1)) // 2
  else:
    ans = 0
  return ans % M


T = int(input())
for i in range(T):
  case = list(map(int, input().split()))
  case[0], case[1] = min(case[0:2]), max(case[0:2])
  print(solve(case))