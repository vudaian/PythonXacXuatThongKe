import numpy as np

x = np.array([2, np.nan, 5, 9])
print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))

print("mean = ", np.mean(x))
print("median = ", np.median(x))