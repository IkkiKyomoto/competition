input = list(map(int, input().split()))
input.sort()
count = 0
while input[0] < input[2] and input[1] < input[2]:
  input[0] += 1
  input[1] += 1
  count += 1
min_input = min(input[0], input[1])
if (input[2] - min_input) % 2 == 0:
  count += (input[2] - min_input) // 2
else:
  count += (input[2] - min_input) // 2
  count += 2
print(count)