N, A, B = map(int, input().split())
ans = 0
A, B = min(A, B), max(A, B)
if abs(A - B) % 2 == 0:
  ans = abs((A - B) // 2)
else:
  if N - B > A - 1:
    ans += A
    B -= A
    ans += (B - 1) // 2
  else:
    ans += N - B + 1
    A += N - B + 1
    ans += (N - A) // 2
  
print(ans)