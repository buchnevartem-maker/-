A = list(map(int, input().split()))

total_sum = sum(A)

product_even_idx = 1
for i in range(0, len(A), 2): 
    product_even_idx *= A[i]

print(total_sum)
print(product_even_idx)