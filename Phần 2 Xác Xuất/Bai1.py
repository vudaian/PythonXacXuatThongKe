import numpy as np
#random.randint
a = np.random.randint(0, 2) # Ngẫu nhiên số nguyên trong khoảng [0, 2)
print("a = ",a)
coins = np.random.randint(2, size=1000)
print(coins.shape)

#Tính % số lần tung được mặt ngửa và úp, ta sẽ thấy nó đều xấp xỉ 50%:
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
