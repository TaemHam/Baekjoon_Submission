# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import permutations
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    
    def match(x):
        if vis[x] == v:
            return 0
        vis[x] = v
        for i in grp[x]:
            if occ[i] == -1 or match(occ[i]):
                occ[i] = x
                return 1
        return 0
    
    stt = []
    grp = []
    N = int(input().strip())
    for num in range(N):
        grp.append([])
        cur = tuple(map(int, input().split()))
        for prv in range(len(stt)):
            if cur[0] >= stt[prv][0] and cur[1] >= stt[prv][1] and cur[2] >= stt[prv][2]:
                grp[num].append(prv)
            if cur[0] <= stt[prv][0] and cur[1] <= stt[prv][1] and cur[2] <= stt[prv][2] and cur != stt[prv]:
                grp[prv].append(num)
        stt.append(cur)

    vis = [-1] * N
    occ = [-1] * N

    for v in range(N*2):
        match(v//2)

    return occ.count(-1)

    # ######## INPUT AREA END ############


# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    print(main())