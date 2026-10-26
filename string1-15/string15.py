s = "abcXYZабвг"
count = sum(
    1 for ch in s
    if ('a' <= ch <= 'z') or ('а' <= ch <= 'я') or ('А' <= ch <= 'Я') and ch.islower()
)
count = sum(1 for ch in s if ch.isalpha() and (ch.islower()))
count = sum(
    1 for ch in s
    if ('a' <= ch <= 'z') or ('а' <= ch <= 'я')
)
print(count)