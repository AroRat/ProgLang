n = int(input())

if n <= 0:
    print("0 0")
    sys.exit()

k = (n + 24) // 25
min_class_size = n // k
print(k, min_class_size)
