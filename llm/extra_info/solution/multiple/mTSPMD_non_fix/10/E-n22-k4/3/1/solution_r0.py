import math
import random
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Cities data
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

depots = [0, 1, 2, 3]
non_depots = [i for i in cities if i not in depots]

# Assigning cities to the closest depot
clusters = {depot: [depot] for depot in depots}  # starts with the depot itself

for city in non_depots:
    closest_depot = min(depots, key=lambda depot: euclidean_distance(cities[city], cities[depot]))
    clusters[closest_depot].append(city)

# Solving TSP for each cluster using 2-opt
def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(distance_matrix[new_route[k]][new_route[k+1]] for k in range(len(new_route) - 1)) < \
                   sum(distance_matrix[best[k]][best[k+1]] for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Create a distance matrix
N = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(N)] for i in range(N)]

# Solve using 2-opt for each cluster
tours = {}
total_cost = 0

for depot, cluster in clusters.items():
    initial_tour = cluster[:] + [depot]  # initial route: depot -> assigned cities -> depot
    tour = two_opt(initial_tour, distance_matrix)
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    tours[depot] = (tour, cost)
    total_cost += cost

# Printing results
for depot, (tour, cost) in tours.items():
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")