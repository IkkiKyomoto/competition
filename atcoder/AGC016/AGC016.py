from collections import defaultdict

s = input()
freq = defaultdict(int)
n = len(s)
ans = 10**7


for e in set(s):
    tmp = s
    count = 0
    while len(set(tmp)) > 1:
        count += 1
        t = ""
        for i in range(len(tmp) - 1):
            if tmp[i] == e or tmp[i + 1] == e:
                t += e
            else:
                t += tmp[i]
        tmp = t
    ans = min(count, ans)
print(ans)
