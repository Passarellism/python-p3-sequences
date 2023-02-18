#!/usr/bin/env python3



def print_fibonacci(length):
    my_list = []
    for n in range(length):
        if n == 0 or n == 1:
            (my_list.append(n))
        else:
            my_list.append(my_list[(n-1)] + my_list[(n-2)])
    print (my_list)

