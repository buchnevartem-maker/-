import os
count = 0
for _ in range(4):
    if os.path.exists(input()):
        count += 1
print(count)