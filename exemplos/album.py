import random

N = 450
n = 4

album = set(range(1,N+1))

count = 0
while len(album) > 0:
    album -= set([random.randint(1, N) for i in range(n)])
    count += 1

print(count)