def is_long_enough(password):
    if len(password) < 8:
        return False
    else:
        return True
print(is_long_enough('1234'))
print(is_long_enough('123456789'))