import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n = int(input_data[0])
idx = 1

for _ in range(n):
    if idx + 8 > len(input_data):
        break
    p1, q1, p2, q2, p3, q3, p4, q4 = map(int, input_data[idx:idx+8])
    idx += 8

    num1 = p1 * q2 + p2 * q1
    den1 = q1 * q2

    num2 = p3 * q4 + p4 * q3
    den2 = q3 * q4

    left = num1 * den2
    right = num2 * den1

    if left > right:
        print(1)
    elif left == right:
        print(0)
    else:
        print(-1)