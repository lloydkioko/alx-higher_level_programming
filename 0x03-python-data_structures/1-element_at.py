#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    else:
        for x in range(0, len(my_list)):
        if x == idx:
            return (my_list[idx])
