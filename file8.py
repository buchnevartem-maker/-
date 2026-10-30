src, dst = input(), input()
with open(src) as f:
    lines = f.read().splitlines()
with open(dst, "w") as f:
    f.write(lines[0] + "\n")
    f.write(lines[-1] + "\n")