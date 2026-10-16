import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

code = input_data[0]
i = 0
n = len(code)
numbers = []

while i < n:
    zeros_count = 0
    while i < n and code[i] == "0":
        zeros_count += 1
        i += 1

    z = zeros_count + 1

    y_bin = code[i : i + z]
    i += z
    y = int(y_bin, 2)

    x_bin_without_leading = code[i : i + y - 1]
    i += y - 1

    x_bin = "1" + x_bin_without_leading
    x = int(x_bin, 2)

    numbers.append(x)

print(len(numbers))
print(*numbers)