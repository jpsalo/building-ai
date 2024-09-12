import random

dogs_prob = 0.8


def main():
    favourite = "dogs"  # change this

    if random.random() < 0.2:
        if random.random() < 0.5:
            favourite = "cats"
        else:
            favourite = "bats"

    print("I love " + favourite)


main()
