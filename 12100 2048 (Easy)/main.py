# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
from collections import deque
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
    global grp, ans
    n = int(input().strip())
    grp = []
    for _ in range(n):
        grp.append(list(map(int, input().split())))
    q = deque()
    ans = 0

    def get(y, x):
        if grp[y][x]:
            q.append(grp[y][x])
            grp[y][x] = 0

    def merge(y, x, dy, dx):
        while q:
            v = q.popleft()
            if grp[y][x] == 0:
                grp[y][x] = v
            elif grp[y][x] == v:
                grp[y][x] = v * 2
                y += dy
                x += dx
            else: #grp[y][x] != v:
                y += dy
                x += dx
                grp [y][x] = v
            
    def move(dir):
        if dir == 0:
            for x in range(n):
                for y in range(n):
                    get(y, x)
                merge(0, x, 1, 0)
        elif dir == 1:
            for x in range(n):
                for y in range(n-1, -1, -1):
                    get(y, x)
                merge(n-1, x, -1, 0)
        elif dir == 2:
            for y in range(n):
                for x in range(n):
                    get(y, x)
                merge(y, 0, 0, 1)
        else: #dir == 3:
            for y in range(n):
                for x in range(n-1, -1, -1):
                    get(y, x)
                merge(y, n-1, 0, -1)

    def solve(cnt):
        global ans, grp
        if cnt == 5:
            for i in range(n):
                ans = max(ans, max(grp[i]))
            return
        
        g = [t[:] for t in grp]

        for d in range(4):
            move(d)
            solve(cnt+1)
            grp = [t[:] for t in g]

    solve(0)
    print(ans)

            



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
    main()