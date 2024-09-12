import numpy as np

data = [
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
]


def distance(row1, row2):
    sum = 0
    for w1, w2 in zip(row1, row2):
        sum = sum + float(abs(w1 - w2))

    if sum == 0:
        sum = np.inf

    return sum


def find_nearest_pair(data):
    # N = len(data)
    # dist = np.empty((N, N), dtype=float)
    dist = np.array([[distance(sent1, sent2) for sent1 in data] for sent2 in data])
    print(np.unravel_index(np.argmin(dist), dist.shape))


find_nearest_pair(data)
