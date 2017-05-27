"""
Created: 26/05/2017
Author: Amartya Gupta
"""

from math import pi, log

num = {0: '0',
       1: '1',
       2: '2',
       3: '3',
       4: '4',
       5: '5',
       6: '6',
       7: '7',
       8: '8',
       9: '9',
       10: 'A',
       11: 'B',
       12: 'C',
       13: 'D',
       14: 'E',
       15: 'F',
       16: 'G',
       17: 'H',
       18: 'I',
       19: 'J',
       20: 'K',
       21: 'L',
       22: 'M',
       23: 'N',
       24: 'O',
       25: 'P',
       26: 'Q',
       27: 'R',
       28: 'S',
       29: 'T',
       30: 'U',
       31: 'V',
       32: 'W',
       33: 'X',
       34: 'Y',
       35: 'Z'}


def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi
    with optional x decimals"""
    # your code here
    result = []  # setting list to capture converted digit
    # check for a proper base
    if base <= 0:
        base = pi
    # if n is zero then set the starting power as zero
    if n != 0:
        s_power = int(log(abs(n), base))
    else:
        s_power = 0

    div = abs(n)  # starting point for iterative division

    if n < 0:
        result.append("-")
    """
    n / base^(S_power - 0) = n1
    R / base^(S_power - 1) = n2 ( R=remainder, change remainder when division
    R / base^(S_power - 0) = n3                               yields > 1)
    ..........
    R / base^(0) = n..
    R / base^(-1) = n..
    ..........
    R / base^(-decimals) = n..
    """

    for i in range(0, (s_power + abs(decimals) + 1)):
        if (s_power - i) == -1:
            result.append(".")
        var = int(div / base**(s_power - i))
        result.append(num[var])
        if var > 0:
            div = div % base**(s_power - i)

    return "".join(result)


print(converter(0, 4, 26))
