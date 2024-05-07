N = int(input())
a = [None] * N
for i in range(N):
    a[i] = int(input())

light = 1
light = a[light - 1]
flag = True
count = 1
already = {1}
while flag:
    if light in already:
        flag = False
        ans = -1
    elif light == 2:
        flag = False
        ans = count
    else:
        already.add(light)
        count += 1
        light = a[light - 1]

print(ans)
