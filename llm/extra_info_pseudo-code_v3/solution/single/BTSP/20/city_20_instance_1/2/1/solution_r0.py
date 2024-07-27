import math

def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Defines the cities' coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

import itertools

def find_min_bottleneck_tour(cities):
    nodes = list(cities.keys())
    edges = [(i, j) for i in nodes for j in nodes if i != j]
    distances = {edge: calc_distance(cities[edge[0]], cities[edge[1]]) for edge in edges}
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])

    for _, bottleneck_distance in sorted_distances:
        for perm in itertools.permutations(nodes):
            valid_tour = True
            max_edge_length = 0
            for i in range(len(perm) - 1):
                if distances[(perm[i], perm[i+1])] > bottleneck_distance:
                    valid_tour = False
                    break
                max_edge_length = max(max_edge_length, distances[(perm[i], perm[i+1])])
            if valid_tour:
                total_cost = sum(distances[(perm[i], perm[i+1])] for i in range(len(perm) - 1))
                return list(perm) + [perm[0]], total_cost, max_edge_length

# Call the function and print results
tour, total_cost, max_distance = find_min_bottleneck_tour(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)