import numpy as np
print("Hello, ML world")
A = np.array([[2,1],[2,4]])
b = np.array([3,5])
x =np.linalg.solve(A, b)
print("Solution of AX = b:",x)
print("Check A @ x:", A @ x)
