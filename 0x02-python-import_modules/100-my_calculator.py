#!/usr/bin/python3
if __name__ == "__main__":
    '''Calculator'''
    #keys() returns a list of all the available keys in the dictionary.
    #opt : library contating the operator symbols and their assingments.
    #sys.argv[1] = a
    #sys.argv[2] = operator
    #sys.argv[3] = b
    import sys
    from calculator_1.py import add,sub,mul,div

    int(a) = 3
    int(b) = 5

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    opt = {'+' : add,'-' : sub,'*' : mult,'/' : div}
    if sys.argv[2] not in list(opt.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a,sys.argv[2], b, opt[sys.argv[2]](a,b)))
