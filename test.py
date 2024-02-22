from numpy import array, arange, nditer
from time import perf_counter_ns

rangee = arange(100)

total = 0
for _ in range(100):
    iterable = nditer(rangee, flags=["f_index"])
    strt = perf_counter_ns()
    for x in iterable:
        x
    nd = perf_counter_ns()
    total += nd - strt
print(total/10)

print("_________________________")

total = 0
for _ in range(100):
    strt = perf_counter_ns()
    for x in range(100):
        x
    nd = perf_counter_ns()
    total += nd - strt
print(total/10)

print("_________________________")

total = 0
for _ in range(100):
    i = 0
    strt = perf_counter_ns()
    while i < 100:
        rangee[i]
        i+=1
    nd = perf_counter_ns()
    total += nd - strt
print(total/10)