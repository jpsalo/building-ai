from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3,
)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42
)

k_values = [133, 1, 250, 42, 100]

for k in k_values:
    # Create a classifier and fit it to our data
    print("k =", k)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    train_acc = knn.score(x_train, y_train)
    print("training accuracy: %f" % train_acc)
    test_acc = knn.score(x_test, y_test)
    print("testing accuracy: %f" % test_acc)
    print("")
