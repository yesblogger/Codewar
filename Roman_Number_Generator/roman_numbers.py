#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:02:44 2017

@author: Amartya Gupta
"""

base = {
                1: {"I": 1, 1: "I",
                    "V": 5, 5: "V"},
                2: {"X": 10, 10: "X",
                    "L": 50, 50: "L"},
                3: {"C": 100, 100: "C",
                    "D": 500, 500: "D"},
                4: {"M": 1000, 1000: "M",
                    "V_": 5000, 5000: "V_"}
            }

        
def logic(n, s):
    if s > 4: 
        return "outrange"
    if n in base[s]:
        return base[s][n]
    else:
        mi = min(i for i in base[s] if type(i) is int)
        mx = mi * 5
        if n < mx:
            if n // mi <= 3:
                return base[s][mi] + logic(n - base[s][base[s][mi]], s)
            else:
                return base[s][mi] + logic(n + base[s][base[s][mi]], s)
        else:
            if (n - mx) // mi <= 3:
                return base[s][mx] + logic(n - base[s][base[s][mx]], s)
            else:
                return base[s][mi] + logic(n + base[s][base[s][mi]], s+1)
            
def solution(n):
    # TODO convert int to roman string
    result = []
    for i in range(1, len(str(n)) + 1):
        temp = n % 10**i
        if temp:
            n -= temp
            result.append(logic(n=temp, s=i))
    return ''.join(result[::-1])
        
        
