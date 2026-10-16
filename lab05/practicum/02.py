import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

t = int(input_data[0])
idx = 1
results = []

for _ in range(t):
    n = int(input_data[idx])
    p = int(input_data[idx + 1])
    q = int(input_data[idx + 2])
    idx += 3

    digits = []
    for _ in range(n):
        p *= 2
        digit = p // q
        digits.append(str(digit))
        p %= q

    results.append("0." + "".join(digits))

print("\n".join(results))