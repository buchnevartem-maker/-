def if5(a, b, c):
    pos_count = 0
    neg_count = 0
    for val in (a, b, c):
        if val > 0:
            pos_count += 1
        elif val < 0:
            neg_count += 1
    return pos_count, neg_count