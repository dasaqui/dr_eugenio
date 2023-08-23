def fact(num):
    #ahora si para cualquier factorial
    if num == 1:
        return 1
    else:
        return num * fact(num-1)
