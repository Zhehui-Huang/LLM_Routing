import itertools
import math

# City coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
          (78, 76), (68, 45), (50, 28), (69, 9)]

# City groups
groups = [[5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_shortest_tour(cities, groups):
    shortest_tour = None
    min_cost = float('inf')

    # Testing every combination of choosing one city from each group
    for comb in itertools.product(*groups):
        # Permutations of the selected cities to visit
        for perm in itertools.permutations(comb):
            path = [0] + list(perm) + [0]  # Start and end at the depot city
            cost = sum(euclidean_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
            
            if cost < min_cost:
                min_cost = cost
                shortest_tour = path

    return shortest_tour, min_cost

tour, total_cost = find_shortest_tour(cities, groups)
print("Tour:", tour)
print("Total travel cost:", total_cost)