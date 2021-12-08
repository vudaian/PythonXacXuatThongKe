import numpy as np

X = [1, 2, 3, 4, 5]
print("Mean X = ", np.mean(X))

X = np.array([[1, 2], [3, 4]])
print("Mean X = ", np.mean(X))
print("Mean X với axis = 0: ", np.mean(X, axis=0))
print("Mean X với axis = 1: ", np.mean(X, axis=1))

a = np.zeros((2, 512 * 512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1

print("a.shape: ", a.shape)
print("mean a = ", np.mean(a))

print("mean a = ", np.mean(a, dtype=np.float64))