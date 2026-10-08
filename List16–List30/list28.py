strings = input().split()
letter = input()

filtered = (s for s in strings if s.startswith(letter))
print(*filtered)