def fibonacci(a):
    if a == 1 or a == 0:
       return a
    else:

       return(fibonacci(a - 1) + fibonacci(a - 2))


if __name__ == '__main__':
    a = 10
    for i in range(0,10):

        print(fibonacci(i))