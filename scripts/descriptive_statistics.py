import statistics as st
import pandas as pd
import numpy as np
import scipy

a = [1, 2, 3, 3]

# sum of numbers
print("sum: {}".format(sum(a)))

# length of a
print("length: {}".format(len(a)))

# how many times 3 appears in a
print("3 appears {} times".format(a.count(3)))

# mean of a
print("mean: {}".format(sum(a)/len(a)))

# mean of a
statistics_mean = st.mean(a)
print("mean: {}".format(statistics_mean))


# median of a
statistics_median = st.median(a)
print("median: {}".format(statistics_median))

# mode of a
mode = st.mode(a)
print("mode: {}".format(mode))

# variance of a
variance = st.variance(a)
print("variance: {}".format(variance))


# standard deviation of a
stndrdev = st.stdev(a)
print("std dev: {}".format(stndrdev))


# IQR
b = st.quantiles(a)
