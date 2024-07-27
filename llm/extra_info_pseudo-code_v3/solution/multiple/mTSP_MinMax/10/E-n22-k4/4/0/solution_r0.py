import numpy as np
from sklearn.cluster import KMeans
import random
import itertools

# Define the cities and their coordinates
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

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial clustering using KMeans
def cluster_cities(n_clusters):
    coords = np.array(list(cities.values()))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coords)
    clusters = {i: [] for i in range(n_clusters)}
    for i, label in enumerate(kmeans.labels_):
        clusters[label].append(i)
    return clusters

# Random Greedy Heuristic
def random_greedy_tour(cluster, starting_point):
    unvisited = set(cluster)
    tour = [starting_point]
    current = starting_point
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current, x))
        if random.random() > 0.5:  # Introducing randomness
            next_city = random.choice(list(unvisited))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(starting_point)
    return tour

# Calculate the total travel cost of a tour
def calculate_travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Main function to solve the problem
def solve_mtsp(num_robots):
    clusters = cluster_cities(num_robots)
    tours = []
    for _, cluster in clusters.items():
        tour = random_greedy_tour(cluster, 0)  # Start and end at the depot
        tours.append(tour)

    costs = [calculate_travel_cost(tour) for tour in tours]
    max_cost = max(costs)

    return tours, costs, max_file_cost, num_robots

if __name__ == "__main__":
    num_robots = 4
    tours, costs, max_travel_cost, num_robots = solve_mtsp(num_robots)

    for i, (tour, cost) in enumerate(zip(tours, costs)):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")

    print(f"Maximum Travel Cost: {max_travel_cost}")