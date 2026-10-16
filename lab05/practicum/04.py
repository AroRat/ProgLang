import sys

def encode_number(x: int) -> str:
    x_bin = bin(x)[2:]
    y = len(x_bin)

    y_bin = bin(y)[2:]
    z = len(y_bin)

    zeros = "0" * (z - 1)
    x_bin_without_leading = x_bin[1:]

    return zeros + y_bin + x_bin_without_leading

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n = int(input_data[0])
numbers = [int(x) for x in input_data[1 : n + 1]]

encoded_parts = [encode_number(x) for x in numbers]

print("".join(encoded_parts))