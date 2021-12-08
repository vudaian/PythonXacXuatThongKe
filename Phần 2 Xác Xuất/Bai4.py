import numpy as np

#random.binomial
b = np.random.binomial(20, 0.5) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print("b = ", b)

array = np.random.binomial(20, 0.5, 10)
print(array)

print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())

n = 10  # tung 10 đồng xu trong 1 lần
p = 0.2  # bias cho mặt ngửa (xác suất cho mặt ngửa là 0.2)
l = 1000  # số lần lặp

b = np.random.binomial(n, p, l)
print("Trung bình số mặt ngửa nhận được: ", b.mean())