def add_right_digit(d, k):
    return k * 10 + d

K = int(input())
D1 = int(input())
D2 = int(input())

K = add_right_digit(D1, K)
print(K)
K = add_right_digit(D2, K)
print(K)