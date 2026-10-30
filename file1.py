import os
S = input()
try:
    open(S, "x").close()
    print(True)
except OSError:
    print(False)