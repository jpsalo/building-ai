# Intermediate
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0

    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    if set(route) == set(range(5)):
                        print(" ".join([portnames[i] for i in route]))


main()

# Advanced
# portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
#
# def permutations(route, ports):
#     if len(ports) == 0:
#         print(' '.join([portnames[i] for i in route]))
#     for i, x in enumerate(ports):
#         route.append(x)
#         ports = ports[:i]+ports[i+1:]
#         permutations(route, ports)
#         if len(route) == len(portnames):
#             if len(ports) == len(range(1, len(portnames))) - 1:
#                 ports = list(range(1, len(portnames)))
#                 route = [0]
#             else:
#                 break
#
#
# # This will start the recursion with 0 ("PAN") as the first stop
# permutations([0], list(range(1, len(portnames))))
