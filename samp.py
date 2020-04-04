import itertools
from random import randint
import numpy as np

def getTrace(arr, K):
    tv = "IMPOSSIBLE"
    diagonal = []
    # for i in set(itertools.permutations(arr)):
    for i in arr:
        if (sum(i) == K):
            diagonal = i
            tv = "POSSIBLE"
            break
    return [tv, diagonal]

def draw_mat(diagonal, N):
    if (diagonal == []):
        return []
    arr = []
    for i in range(N):
        j = []
        for k in range(N):
            m = 1
            while m<N:
                if (m not in j):
                    break
                m += 1
            j.append(m)
        arr.append(j)
    for i in range(N):
        arr[i][i] = diagonal[i]
    return arr


for x in range(1, int(input())+1):
    a = input().split(" ")
    N = int(a[0])
    K = int(a[1])
    del a
    det = getTrace( [ [i for j in range(1, N+1)] for i in range(1, N+1)] , K)
    print("Case #%s: %s" % (x, det[0]))
    for i in draw_mat(det[1], N):
        if (det[0] == 'IMPOSSIBLE'):
            continue
        r = ""
        for j in i:
            r = "%s %s" % (r, j)
        print(r)