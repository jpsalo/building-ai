import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], [21, 3, 50, 1, 100], [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array(
    [
        [3000, 200, -50, 5000, 100],
        [2000, -250, -100, 150, 250],
        [3000, -100, -150, 0, 150],
    ]
)


def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        predicted_price = xi @ c
        difference_square = (yi - predicted_price) ** 2
        sse += difference_square
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi,
        # square the difference using (yi - prediction)**2,
        # and add up all the differences in variable sse

    print(sse)


def find_best(X, y, c):
    smallest_error = np.inf
    best_index = -1
    for i, coeff in enumerate(c):
        predicted_prices = X @ coeff
        difference_square = sum(np.square(np.subtract(y, predicted_prices)))
        if difference_square < smallest_error:
            smallest_error = difference_square
            best_index = i
        # pass     # edit here: calculate the sum of squared error with coefficient set coeff and
        # keep track of the one yielding the smallest squared error
    print("the best set is set %d" % best_index)


real_c = np.linalg.lstsq(X, y)[0]
print(real_c)

find_best(X, y, c)
