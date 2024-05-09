N = int(input())
pos_x = 0
pos_y = 0
time = 0
flag = True
for i in range(N):
  t, x, y = map(int, input().split())
  sub_t = t - time
  sub_x = abs(x - pos_x)
  sub_y = abs(y - pos_y)
  if sub_t >= sub_x + sub_y and sub_t % 2 == (sub_x + sub_y) % 2:
    pos_x = x
    pos_y = y
    time = t
  else:
    flag = False
    break
print("Yes" if flag else "No")
    