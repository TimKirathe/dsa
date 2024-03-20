# Task: Find minimum of function f = (x - 3)^2 - 1

# Start with x = 0 and learning rate g = 0.2
x = 0
g = 0.1

# Derivative of f = (x - 3)^2 - 1
def derivative(x):
    return 2*(x - 3)

for _ in range(60):
    x = x - g*(derivative(x))

print(x)


# Task: Fitting a function to data

# Coordinates are formatted in list as: x, y
data_points = {"A": [2, 2], "B": [3, 4], "C": [4, 3.5], "D": [6, 6], "E": [6.5, 5]}
data_points_x = [2,3,4,6,6.5]
data_points_y = [2,4,3.5,6,5]
# Assume function that fits these points is linear, in form: f = w_0 + w_1x

# Use linear least squares loss function obtaining:
# 0 = 5(w_0)^2 + 43w_0w_1 - 41w_0 - 197w_1 + 107.5(w_1)^2 + 93.25

# Since weights are in 2 dimensions, answer will be a 2-D vector of weights, 
# therefore need to compute derivative with respect to both weights individually.

# Expression for dO/dw_0
def derivative_w0(w0, w1):
    return 10 * w0 + 43 * w1 - 41

# Expression for dO/dw_1
def derivative_w1(w0, w1):
    return 215 * w1 + 43 * w0 - 197

weight_vector = [0, 0]
# g2 = 0.0005
g2 = 0.001

for _ in range (1000000):
    w0 = weight_vector[0]
    w1 = weight_vector[1]
    print(w0)
    print(w1)
    weight_vector[0] = w0 - g2 * derivative_w0(w0, w1)
    weight_vector[1] = w1 - g2 * derivative_w1(w0, w1)

print(weight_vector)

import matplotlib.pyplot as plt
import numpy as np

plt.scatter(data_points_x,data_points_y)
plt.xlabel('x')
plt.ylabel('y')

x_coords = np.linspace(0,10,100)

y_coords = weight_vector[0] + weight_vector[1] * x_coords

plt.plot(x_coords, y_coords, label=f'Model Prediction: y = {weight_vector[0]} + {weight_vector[1]}x')

plt.legend()
plt.grid(True)
plt.show()
