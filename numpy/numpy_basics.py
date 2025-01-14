import numpy as np


# array =np.array([1,2,3,4,5,6,7,8,9,10,11,12])


# print(array.shape)


# a=array.reshape(3,4)

# print(a)
# print("Shape:" ,a.shape)
# print("Dimension:", a.ndim)
# print("Data type:", a.dtype)
# print("Size:", a.size)
# print("Type:", type(a))

# arra1=np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(arra1.shape)

# zeros= np.zeros((3,4))#allocation of zeros

# zeros[0,0]=58
# print(zeros)

# np.ones((3,4))#allocation of ones

# np.empty((2,3))#allocation of empty

# c=np.arange(10,50,5)

# print(c)

# d=np.linspace(10,50,20)

# print(d)


#numpy basic operations
a=np.array([1,2,3])
b =np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

print(a<2)

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

#element wise product
print(a*b)

a=np.random.random((5,5))
print(a)


print(a.sum())
print(a.max())
print(a.min())

print(a.sum(axis=0))

print(np.sqrt(a))
print(np.square(a))