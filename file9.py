a, b = input(), input()
import os
src, dst = (a, b) if os.path.exists(a) else (b, a)
with open(src) as f:
    lines = f.read().splitlines()
with open(dst, "w") as f:
    f.write(lines[-1] + "\n")
    f.write(lines[0] + "\n")