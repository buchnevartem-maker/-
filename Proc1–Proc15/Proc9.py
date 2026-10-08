def add_left_digit(d, k):
    return int(str(d) + str(k))

K = int(input())
D1 = int(input())
D2 = int(input())

K = add_left_digit(D1, K)
print(K)
K = add_left_digit(D2, K)
print(K)