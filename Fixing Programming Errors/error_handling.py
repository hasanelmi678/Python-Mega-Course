def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'You are dividing by 0'

print(divide(1, 0))
print('End of program')