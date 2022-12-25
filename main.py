from random import randrange

def function_test():

    C = 0

    while C != 4:
        A = randrange(1, 9)
        B = randrange(1, 9)
        C = A * B
        print("value of C is", C, "value of A is", A)
    if C == 4:
        print("success")
        print("value of A is ", A, "value of B is ", B)


if __name__ == '__main__':
    function_test()
