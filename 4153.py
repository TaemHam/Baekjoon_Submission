import sys
arr = []
while True:
    a = sys.stdin.readline().strip()
    if a == '0 0 0': break
    arr += [sorted(list(map(int,a.split())))]
for i in arr:
    if i[0]**2 + i[1]**2 == i[2]**2: print('right')
    else: print('wrong')