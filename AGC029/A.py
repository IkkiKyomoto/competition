S = input()
N = len(S)
B_num = sum(s == "B" for s in S)
ans = 0
for i in range(N):
  if S[i] == "B":
    ans += N - B_num - i
    B_num -= 1
print(ans)