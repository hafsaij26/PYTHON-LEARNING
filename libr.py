import numpy as np
import pandas as pd

n= np.array([1, 2, 3])
print(n)
print(type(n))
print(n.shape)
print(n[0])
print(n[-1])
print(n.size)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[1,1])
print(arr(1))
print(arr[:,2])
arr[2,1]=100
#random
ar=np.random.randint(1,100,10)
print(ar)
ar=np.random.randint(1, 100,(3,3))
print(ar)
print("average is ", np.mean(ar))
print("sum is ", np.sum(ar))
print("max is ", np.max(ar))
print("lowest is:", np.min(ar))
data = {
    "Student": ["A", "B", "C", "D"],
    "Age": [19, 20, 21, 18],
    "Marks": [75, 88, 92, 64]
}

df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df["Marks"])