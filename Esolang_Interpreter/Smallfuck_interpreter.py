"""
Created: 17/05/2017
Author: Amartya Gupta
"""


def interpreter(code, tape):
    # Implement your interpreter here
    tape = [i for i in tape]  # breaking the tape in a list
    # declaring the variable to track order
    t_index = c_index = 0  # index value of code and tape
    r_point, brac_count = [], 0  # index values to track [ and ] places

    while 0 <= t_index < len(tape) and c_index < len(code):
        if code[c_index] == '>':  # move index of tape to the right
            t_index, c_index = t_index + 1, c_index + 1
        elif code[c_index] == '<':  # move index of tape to the left
            t_index, c_index = t_index - 1, c_index + 1
        elif code[c_index] == '*':  # invert cell bit if foud *
            tape[t_index] = (lambda x: '1' if x == '0' else '0')(
                tape[t_index])
            c_index += 1
        # Jump past matching ] if value at current cell is 0
        elif code[c_index] == '[':
            if tape[t_index] == '0':
                brac_count += 1  # counter start at zero
                while brac_count != 0:  # code index skips past ']'
                    c_index += 1
                    if code[c_index] == '[':
                        brac_count += 1
                    elif code[c_index] == ']':
                        brac_count -= 1
                c_index += 1
            else:
                r_point.insert(0, c_index)
                c_index += 1
        # Jump back to matching [ (if value at current cell is nonzero)
        elif code[c_index] == ']':
            if tape[t_index] != '0':
                c_index = r_point[0]
            else:
                c_index += 1
                r_point.pop(0)
        else:
            c_index += 1

    return ''.join(tape)
