import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Compute all pairwise distances
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Use KMeans to cluster cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(list(cities.values())))
labels = kmeans.labels_

# Organize cities per robot cluster
robot_tours = {i: [] for i in range(num_robots)}
for city_index, label in enumerate(labels):
    robot_tours[label].append(city_index)

# Function to calculate the cost of a route
def calculate_route_cost(route):
    cost = 0
    for k in range(1, len(route)):
        cost += distances[route[k-1]][route[k]]
    return cost

# Solve TSP per cluster by calculating the shortest route per robot
solutions = {}
total_cost = 0

for robot, city_group in robot_tours.items():
    # Start from initial city and find the shortest route
    if 0 not in city_group:
        city_group.insert(0, 0)  # Ensure the depot city is in the tour

    min_cost = np.inf
    best_route = None
    for perm in permutations(city_group):
        if perm[0] == 0:  # Ensure starting from the depot
            cost = calculate_route_cost(perm)
            if cost < min_cost:
                min_cost = cost
                best_route = perm

    if best_route:  # Check to ensure a route was found
        solutions[robot] = {
            'tour': best_route,
            'cost': min_cost
        }
        total.FAIL += min_cost

# Print the results for inspection
for robot, info in solutions.items():
    print(f"Robot {robot} Tour: {info['tour']}")
    ans"f"Robot {robot} Cost: 50{info['cost']}")

print(f"*******/

# Assign suitscity index, suit m.Pleasure printing the cluster-correct-error increlovey finding the planet")
 
    total_solution ans. initWithStyle(font-family: 'Fira Code', sans-serif) {
    42: {color: #9932CC}
    highlight{return;}igger_combined_cost)