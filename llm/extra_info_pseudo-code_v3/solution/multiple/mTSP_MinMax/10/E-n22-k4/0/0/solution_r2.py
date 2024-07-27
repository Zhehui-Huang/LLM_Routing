import numpy as np
from sklearn.cluster import KMeans

# Coordinates of Cities (excluding the depot city for clustering)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def calculate_distance(city1, city2):
    """ Calculates the Euclidean distance between two cities based on their coordinates. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_clusters(k=4):
    """ Initialize clusters using K-Means algorithm, exclude the depot city. """
    city_locations = np.array([cities[i] for i in range(1, len(cities))])  # exclude depot
    kmeans = KMeans(n_clusters=k, random_state=0).fit(city_locations)
    clusters = {i: [] for i in range(k)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # city indices start from 1 in `clusters`
    return clusters

def construct_tour(initial_city, city_list):
    """ Constructs a greedy tour starting and ending at the initial city. """
    tour = [initial_city]
    current_city = initial_city
    remaining_cities = set(city_list)
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    tour.append(initial_city)  # return to depot
    return tour

def compute_tour_cost(tour):
    """ Computes the cost of a given tour based on distance. """
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

clusters = initialize_clusters()

robot_tours = {}
robot_costs = {}

# Construct and evaluate tours for each cluster/robot
for robot_id, cities_cluster in clusters.items():
    tour = construct_tour(0, cities_cluster)
    cost = compute_tour_cost(tour)
    robot_tours[robot_id] = tour
    robot_costs[robot_id] = cost

# Determine which robot has the maximum travel cost
max_cost = max(robot_costs.values())

# Output tours and costs
for robot_id in robot_tours:
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_cost}")