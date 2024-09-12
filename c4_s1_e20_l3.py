import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-0.5, 0.1, 0.08])
c2 = np.array([-0.2, 0.2, 0.31])
c3 = np.array([0.5, -0.1, 2.53])


def linear(x, c):
    return sum(x * c)


def sigmoid(z):
    # add your implementation of the sigmoid function here
    # s(z)=1÷(1+exp(−z))
    s_z = 1 / (1 + math.exp(-z))
    print(s_z)


# calculate the output of the sigmoid for x with all three coefficients

lin1 = linear(x, c1)
lin2 = linear(x, c2)
lin3 = linear(x, c3)

sig1 = sigmoid(lin1)
sig2 = sigmoid(lin2)
sig3 = sigmoid(lin3)
