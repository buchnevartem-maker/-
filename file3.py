name = input()
A, D = map(float, input().split())
with open(name, "w") as f:
    for i in range(10):
        f.write(str(A + i * D) + "\n")