import numpy as np
from io import StringIO

input_string = """
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
"""

np.set_printoptions(
    precision=1
)  # this just changes the output settings for easier reading


def fit_model(input_file):
    file = np.genfromtxt(input_file, skip_header=1)
    # rint(file)
    prices = file[:, -1]
    x = file[:, :-1]
    # print(prices)
    # Please write your code inside this function

    c = np.linalg.lstsq(x, prices)[0]
    # print(c)
    # print(x @ c)

    # read the data in and fit it. the values below are placeholder values
    # c = np.asarray([])  # coefficients of the linear regression
    # x = np.asarray([])  # input data to the linear regression

    print(c)
    print(x @ c)


# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
