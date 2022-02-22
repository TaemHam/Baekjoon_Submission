# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
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

    n = int(input().strip())
    arr = [int(1e9)] + list(map(int, input().split()))
    h = 2**len(format(n-1, 'b'))
    tree = [int(1e9)] * (h*2)

    h -= 1
    for i in range(1, len(arr)):
        tree[h+i] = arr[i]
    
    for i in range(h, 0, -1):
        tree[i] = min(tree[2*i], tree[2*i+1])

    m = int(input().strip())
    for _ in range(m):
        a, b, c = map(int, input().split())
        
        if a == 1:
            arr[b] = c
            b += h
            tree[b] = c
            while b > 1:
                b >>= 1
                tree[b] = min(tree[b*2], tree[b*2+1])

        else:
            r = int(1e9)
            bt = b+h
            ct = c+h
            while bt <= ct:
                if bt % 2:
                    r = min(r, tree[bt])
                    bt += 1
                if not ct % 2:
                    r = min(r, tree[ct])
                    ct -= 1
                bt //= 2
                ct //= 2
            
            for i in range(b, c+1):
                if arr[i] == r:
                    print(i)
                    break

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