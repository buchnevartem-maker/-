def boolean15(A, B, C):
    pos_count = 0
    if A > 0: pos_count += 1
    if B > 0: pos_count += 1
    if C > 0: pos_count += 1
    return pos_count == 2