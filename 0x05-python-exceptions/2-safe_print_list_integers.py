#!/usr/bin/python3
#num : real number of elements printed
def safe_print_list_integers(my_list=[], x=0):
    num = 0;
    for i in range(x):
    try:
            print("{:d}".format(my_list[i]),end='')
            num += 1
    except (ValueError,TypeError):
        num += 1
        continue
    print("")
    return(num)