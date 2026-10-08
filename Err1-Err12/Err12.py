user_input = input()

try:
    number = int(user_input)
    print(number)
except Exception as e:
    print(type(e).__name__)
    print(e)