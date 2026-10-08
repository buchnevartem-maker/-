def invert_digits(k):
    return int(str(k)[::-1])

for _ in range(5):
    k = int(input())
    print(invert_digits(k))