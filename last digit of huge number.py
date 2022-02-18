# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:07:57 2022

@author: 91838
"""
def last_digit(lst):
    if lst == []:
        return 1
    result = 1
    for num in lst[::-1]:
        result = num ** (result if result < 4 else result % 4 + 4)
        print(result,"gg")
    return result % 10


