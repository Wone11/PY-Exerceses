def factorial(num):
    factor = num
    while(num > 1):
         num = num-1
         factor = factor * num
    return factor

print(factorial(6))