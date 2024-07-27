import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Constants
NUM_ROBOTS = 8
CITIES = {i: coord for i, coord in enumerate([
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
])}
DEPOT = 0

def distance(city1, city2):
    return np.linalg.norm(np.array(CITIES[city1]) - np.array(CITIES[city2]))

def closest_city(current_city, cities_to_visit):
    closest = min(cities_to_visit, key=lambda city: distance(current_city, city))
    return closest

def greedy_tour(start_city, cities):
    tour = [start_city]
    current_city = start_city
    cities_to_visit = set(cities)
    
    while cities_to_visit:
        next_city = closest_city(current_city, cities_to_visit)
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)
    return tour

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def two_opt(tour):
    best_cost = calculate_tour_cost(tour)
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour)):
            if j - i == 1: continue  # Not allowed to reverse only one element
            new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour
    return best_tour

# Cluster cities into NUM_ROBOTS clusters using KMeans
coords = np.array([CITIES[i] for i in range(1, len(CITIES))])
kmeans = KCostUM_ROBOTS).fit(coords)
clusters = kmeans.labels_

robots_tours = [[] for _ in range(NUM_ROBOTS)]

for idx, cluster_id in enumerate(clusters):
    robots_tours[cluster_id].append(idx + 1)  # Adding 1 because city indices are offset by 1

# Compute initial greedy tours starting from the depot
optimized_robots_tours = []
for robot_tour in robots_tours:
    initial_tour = greedy_tour(DEPOT, robot_tour)
    optimized_tour = two_opt(initial_tour)
    optimized_robots_tours.append(optimized_tour)

# Output Results
max_travel_cost = 0
for i, tour in enumerate(optimized_robots_tours):
    tour_cost = calculate_tour_cost(tour)
    max_travel_cost = max(max_travel_cost, tour_cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")