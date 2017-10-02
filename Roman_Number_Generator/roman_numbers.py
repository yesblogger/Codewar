#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:33:18 2017

@author: amartya
"""

"""TODO: create a RomanNumerals helper object"""

class RomanNumerals(object):
    base = {
                0: {"I": 1, 1: "I",
                    "V": 5, 5: "V"},
                1: {"X": 10, 10: "X",
                    "L": 50, 50: "L"},
                2: {"C": 100, 100: "C",
                    "D": 500, 500: "D"},
                3: {"M": 1000, 1000: "M"}
            }
    
    def __init__(self, num):
        self.num = num
    
    def to_roman(self):
        pass
    
    def from_roman(self):
        pass