def is_square(k):
    if k < 1:
        return False
    root = int(k ** 0.5)
    return root * root == k

count = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        count += 1
print(count)