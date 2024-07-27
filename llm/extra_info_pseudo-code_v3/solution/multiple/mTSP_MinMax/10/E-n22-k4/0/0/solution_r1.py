import numpy as la
from sklearn.cluster import KMeans

# Coordinates of Cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def calculate_distance(city1, city2):
    """ Euclidean distance between two cities based on their coordinates. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_clusters(k=4):
    """ Cluster the cities using K-means clustering, excluding the depot city. """
    data = np.array([cities[i] for i in cities if i != 0])  # exclude depot city from clustering
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    clusters = {i: [] for i in range(k)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # +1 because city indices are reduced by 1 in data array
    return clusters

def greedy_tour(initial_city, cities):
    """ Create a tour starting from the initial city using a greedy algorithm. """
    tour = [initial_city]
    current_city = initial_city
    remaining_cities = set(cities)
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        remaining_cities.remove(next_msg)
        current_city = next_city
        
    tour.append(initial_city)  # return to the starting city
    return tour

def calculate_tour_cost(tour):
    """ Calculate the total cost of a single tour. """
    total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

clusters = initialize_clusters(k=4)
robot_tours = {}
robot_costs = {}

for robot_id, cluster in clusters.items():
    tour = greedy_tour(0, cluster)
    tour_cost = calculate_tour_cost(tour)
    robot_tours[robot_id] = tour
    robot_costs[robot_id] = tour_cost

max_travel_cost = max(robot_costs.values())

# Output the tours and costs
for robot_id in robot_tours:
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_travel_cost}")