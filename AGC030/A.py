A, B, C = map(int, input().split())
if A + B >= C:
  print(C + B)
else:
  print(A + 2* B + 1)