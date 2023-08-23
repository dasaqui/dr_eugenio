def fact( num):
    # This code is to calculate the factorial of a number
    if num == 1:
        return 1
    else:
        return num * fact( num - 1)
