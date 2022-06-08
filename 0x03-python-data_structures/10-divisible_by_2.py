#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = my_list[:]
    for count, value in enumerate(my_list):
        if value % 2 == 0:
            list[count] = "true"
        else:
            list[count] = "false"
        print(list)
