import math
import random  # just for generating random mountains

# generate random mountains

w = [0.05, random.random() / 3, random.random() / 3]
h = [
    1.0
    + math.sin(1 + x / 0.6) * w[0]
    + math.sin(-0.3 + x / 9.0) * w[1]
    + math.sin(-0.2 + x / 30.0) * w[2]
    for x in range(100)
]

h.append(3)


def climb(x, h):
    stepcount = 0
    start_x = x
    summit_x = x
    x_r = x
    x_l = x

    # print('start x', h[x])
    # print('')

    for x_new in range(max(0, x - 5), min(99, x + 5)):
        if h[x_new] > h[x]:
            x = x_new
            print("updated")

    return x

    # while stepcount < 5:
    #     stepcount += 1

    #     x_r_next = x_r + 1
    #     if x_r_next < len(h):
    #         if x_r + 2 < len(h) and h[x_r_next] > h[x_r + 2]:
    #             if h[x_r_next] > h[start_x] and h[x_r_next] > h[summit_x]:
    #                 # print('prev summit', h[summit_x])
    #                 # print('new summit to right', h[x_r_next])
    #                 # print('step count', stepcount)
    #                 # print('')
    #                 summit_x = x_r_next
    #     x_r = x_r_next

    #     x_l_next = x_l - 1
    #     if x_l_next >= 0:
    #         if x_l - 2 >= 0 and h[x_l_next] > h[x_l - 2]:
    #             if h[x_l_next] > h[start_x] and h[x_l_next] > h[summit_x]:
    #                 # print('prev summit', h[summit_x])
    #                 # print('new summit to left', h[x_l_next])
    #                 # print('step count', stepcount)
    #                 # print('')
    #                 summit_x = x_l_next
    #     x_l = x_l_next

    # # print('summit x', h[summit_x])
    # return summit_x


def main(h):
    # start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("start", h[x0])
    print("end", h[x])

    return x0, x


main(h)
