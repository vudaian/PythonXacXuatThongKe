import numpy as np

X = np.array([2, 5, 3, 1, 7])
Y = np.array([2, 1, 8, 5, 7, 9])

print("Median X = ", np.median(X))
print("Median Y = ", np.median(Y))

arr = np.array([[7, 4, 2], [3, 9, 5]])
print("median arr (axis = 0) = ", np.median(arr, axis=0))
print("median arr (axis = 1) = ", np.median(arr, axis=1))

freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 2121, 3462])
print("Số người truy cập trung bình mỗi ngày trong tuần qua của Freetuts: ", np.mean(freetuts_visitors))

freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 50293, 30432]) # 2 giá trị cuối lệch xa so với các giá trị trong dãy
print("Mean = : ", np.mean(freetuts_visitors))
print("Median = : ", np.median(freetuts_visitors))