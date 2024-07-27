import numpy as np
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
    data = np.array([cities[i] for i in range(1, len(cities))])
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    clusters = {i: [] for i in range(k)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # +1 to match city index (excluding depot)
    return clusters

def greedy_tour(initial_city, cities):
    """ Create a tour starting from a city, visiting all specified cities minimally. """
    tour = [initial_city]
    current_city = initial.city
    remaining_cities = set(cities)
    remaining_cities.remove(initial_city)
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
        
    tour.append(initial_city)  # return to starting city
    return tour

def calculate_tour_cost(tour):
    """ Calculate the total cost of a single tour. """
    total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

def iterated_local_search(tour):
    """ Perform simple local search to try and improve the tour. Placeholder for more complex VNS. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # consecutive cities, skip
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

# Initialize and solve the mTSP with clustering
clusters = initialize_clusters()
robot_tours = {}
robot_costs = {}

# Assign initial tours to robots
for robot, cluster_cities in clusters.items():
    tour = greedy_tour(0, cluster_cities)
    improved_tour = iterated_local_search(tour)
    robot_tours[robot] = improved_tour
    robot_costs[robot] = calculate_tour_cost(improved_tour)

# Find the robot with the maximum travel cost
max_travel_cost = max(robot_costs.values())

# Output results
for robot, tour in robot_tours.items():
    cost = robot_costs[robot]
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_controller}")