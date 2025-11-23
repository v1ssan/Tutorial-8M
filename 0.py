'''
This file contains a broken bubble implementation.

Tasks:
 - Run broken_bubble on [3,1,2] to see the problem.
 - Fix the bug.

'''

def broken_bubble(arr):
    a = arr[:]
    n = len(a)
    comps = swaps = 0

    for i in range(n):
        for j in range(0, n):
            comps += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    return a

