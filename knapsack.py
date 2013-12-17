from __future__ import division
from heapq import heappush, heappop
from itertools import count

def bb_knapsack(w, v, c):
    sol = 0
    n = len(w)

    idxs = list(range(n))
    idxs.sort(key=lambda i:v[i]/w[i],
              reverse = True)


