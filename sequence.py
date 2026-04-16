# (1)
# Complete the sequence_calculator function, which should
# Return the n-th number of the sequence S_n, defined as:
# S_n = 3*S_(n-1) - S_(n-2), with S_0 = 0 and S_1 = 1.
# Your implementation should minimize the execution time.
#
# (2)
# Find the time complexity of the proposed solution, using
# the "Big O" notation, and explain in detail why such
# complexity is obtained, for n ranging from 0 to at least
# 100000. HINT: you are dealing with very large numbers!
#
# (3)
# Plot the execution time VS n (again, for n ranging from 0
# to at least 100000).
#
# (4)
# Confirm that the empirically obtained time complexity curve
# from (3) matches the claimed time complexity from (2) (e.g.
# by using curve fitting techniques).

import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def sequence_calculator(n):
    if n==0 or n==1:
        return n
    curr, prev=1, 0
    for i in range(2, n+1, 1):
        prev, curr=curr, 3*curr-prev
    return curr

intervals=[]
n_values = np.unique(np.logspace(0, 5, 200, dtype=int))
for i in tqdm(n_values):
    start=time.time()
    sequence_calculator(i)
    end=time.time()
    intervals.append(end-start)

np.save("timings.npy", np.array(intervals))

coeffs = np.polyfit(n_values, intervals, 2)
fit = np.polyval(coeffs, n_values)

plt.scatter(n_values, intervals, label="measured")
plt.plot(n_values, fit, label="quadratic fit")
plt.legend()
plt.show()