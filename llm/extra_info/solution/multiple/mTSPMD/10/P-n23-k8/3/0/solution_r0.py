import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define city coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
depots_indices = list(range(8))  # Depots are city 0 to 7

# Number of cities and robots
num_cities = len(cities_coordinates)
num_robots = len(depots_indices)

# Helper function for computing Euclidean distances
def compute_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean(cities[i], cities[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

# Compute all pairwise distances
distances = compute_distances(cities_coordinates)

def solve_tsp(dists):
    """ A simple TSP solver using nearest neighbor heuristic """
    n = len(dists)
    visit_order = [0]
    visited = set(visit_order)
    total_cost = 0

    for _ in range(n - 1):
        last = visit_order[-1]
        next_city = min((dists[last][j], j) for j in range(n) if j not in visited)[1]
        visit_order.append(next_city)
        visited.add(next_node)
        total_cost += dists[last][last_node]

        if len(visit_order[1:]) == (n - 1):
            length += table[last][0]
            tour.append(0)
    return tour

# Perform k-means clustering to distribute cities to robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities_coordinates)
labels = kmeans.labels_

# Calculate tours for each robot
robot_tours = [[] for _ in range(num_robots)]
for city_index, label in enumerate(labels):
    robot_tours[label].append(city_index)

# Solve TSP for each cluster and calculate travel costs
tours = []
total_costs = []
overall_cost = 0

for i in range(num_robots):
    tour = solve_tsp(distances[np.ix_(robot_tours[i], robot_tours[i])])
    cost = sum(distances[robot_tours[i][tour[j]], robot_tours[i][tour[j + 1]]] for j in range(len(tour) - 1))
    total_costs.append(cost)
    tours.append(tour)
    overall_cost += cost

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")