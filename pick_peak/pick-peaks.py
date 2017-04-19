"""
Created: 18/04/2017
Author: Amartya Gupta
"""


def pick_peaks(arr=[-1, 1, -5, 17, -2, 10, -1, 5, 7, 11, 17, 18, 0, -2, 5, 11]):
    # marking up trend and plateaus as one and down trend as zero
    trend = [1 if i <= j else 0 for i, j in zip(arr, arr[1:])]
    # capturing the position of all the peaks in the trend
    pos = [k + 1 for i, j, k in zip(trend, trend[1:], range(len(arr)))
           if i == 1 and j == 0]
    # identifying plateaus for local maxima, excluding extreme points
    fales_peak = []
    for j, i in enumerate(pos):
        count = 1
        while True:
            if arr[i] != arr[i - count] or pos[j] == 0:
                if arr[i - (count - 1)] < arr[i - count] or pos[j] == 0:
                    fales_peak.append(pos[j])
                break
            else:
                pos[j] = i - count
                count += 1
    # deletion of fales peak
    for i in fales_peak:
        pos.remove(i)
    # peak declaration
    peak = [arr[i] for i in pos]
    return {'pos': pos, 'peaks': peak}


print(pick_peaks())
