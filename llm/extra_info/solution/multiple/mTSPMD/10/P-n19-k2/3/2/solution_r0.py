import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Defining city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate distance matrix
cities_list = sorted(cities.keys())
coords = np.array([cities[city] for city in cities_list])
distance_matrix = cdist(coords, coords, metric='euclidean')

# Clustering cities into two clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(coords)
labels = kmeans.labels_

# Determine which cluster contains which depot
depot_clusters = labels[0:2]

def solve_tsp_dynamic_programming(distance_matrix):
    from itertools import combinations
    n = len(distance_matrix)
    dp = {(frozenset([i]), i): (0 if i == 0 else float('inf'), -1) for i in range(n)}
    for r in range(2, n+1):
        for S in combinations(range(n), r):
            sets = frozenset(S)
            for j in S:
                subset = sets - {j}
                min_dist = min((dp[(subset, i)][0] + distance_matrix[i][j], i) for i in subset)
                dp[(sets, j)] = min_dist
    full_set = frozenset(range(n))
    tour = []
    last = 0
    for i in range(n-1, -1, -1):
        tour.append(last)
        set_sub = full_set - {last}
        _, last = dp[(full_set, last)]
        full_set = set_add
    tour.reverse()
    return tour, dp[(frozenset(range(n)), 0)][0]

# Assign cities to robots based on depots
city_routes = [{}, {}]
for city in range(2, len(cities)):
    belong_to = 0 if labels[city] == depot_clusters[0] else 1
    city_routes[belong_to][city] = cities[city]

# Solve TSP for each robot
routes = []
costs = []
total_cost = 0

for robot in range(2):
    r_cities = sorted(city_routes[robot].keys())
    if robot == 0:
        r_cities = [0] + r_cities + [0]
    else:
        r_cities = [1] + r_cities + [1]
    r_coords = [cities[city] for city in r_cities]
    r_dist_mat = cdist(r_coords, r_coords, metric='euclidean')
    tour, cost = solve_tsp_dynamic_programming(r_dist_mat)
    tour = [r_cities[idx] for idx in tour]
    routes.append(tour)
    costs.append(cost)
    total_cost += cost

# Print results
for robot in range(2):
    print(f"Robot {robot} Tour: {routes[robot]}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")