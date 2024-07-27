import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define the number of robots and their respective depots
num_robots = 4
depots = [0, 1, 2, 3]

# Calculate distances between all pairs of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

dist_matrix = calculate_distances(cities)

# Cluster cities into groups using K-means clustering targeting the depots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[:num_robots])  # only fit to depots to initialize
clusters = kmeans.predict(cities)  # predict all cities

# Assign cities to each robot based on cluster mapping
robot_city_map = {i: [] for i in range(num_robots)}
for city_index, cluster_index in enumerate(clusters):
    robot_city_map[cluster_index].append(city_index)

# Function to compute the total travel cost of a tour
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Finding the best possible tour for each robot using a simple heuristic
def find_tour_for_robot(depot, cities):
    best_tour = None
    best_cost = float('inf')
    # Generate all permutations of the cities and calculate the distance
    for perm in permutations(cities):
        tour = [depot] + list(perm) + [depot]
        cost = tour_cost(tour, dist_matrix)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Solve the TSP for each robot and accumulate the results
overall_cost = 0
results = []
for robot_id in range(num_robots):
    tour, cost = find_tour_for_robot(depots[robot_id], robot_city_map[robot_id])
    results.append((robot_id, tour, cost))
    overall_cost += cost

# Display the results
for robot_id, tour, cost in results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_resources={3} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")