N = int(input())
S = input()
left_to_right = [0 for _ in range(N)]
right_to_left = [0 for _ in range(N)]
turned = [0 for _ in range(N)]
for i in range(1, N):
    if S[i - 1] == "W":
        left_to_right[i] = left_to_right[i - 1] + 1
    else:
        left_to_right[i] = left_to_right[i - 1]
    if S[-i] == "E":
        right_to_left[-i - 1] = right_to_left[-i] + 1
    else:
        right_to_left[-i - 1] = right_to_left[-i]
for i in range(N):
    turned[i] = left_to_right[i] + right_to_left[i]
print(min(turned))
