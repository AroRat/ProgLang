current_value = 1

for letter_code in range(ord('a'), ord('z') + 1):
    letter = chr(letter_code)

    for num in range(100):
        var_name = f"{letter}{num}"
        globals()[var_name] = current_value
        current_value += 1

print("a0:", a0)
print("b0:", b0)
print("z99:", z99)