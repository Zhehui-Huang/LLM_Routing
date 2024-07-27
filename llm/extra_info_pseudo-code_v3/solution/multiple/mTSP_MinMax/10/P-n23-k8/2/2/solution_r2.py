import numpy as np
import random
from scipy.spatial.distance import euclidean

# Initialize cities' coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

def distance(c1, c2):
    return euclidean(cities[c1], cities[c2])

def cluster_cities(num_clusters):
    city_indices = list(cities.keys())[1:]  # Exclude depot
    random_centers = random.sample(city_indices, num_clusters)
    clusters = {i: [] for i in range(num_clusters)}
    
    # Assign each city to the closest cluster center
    for city in city_daty_indices:
        closest_center = min(random_centers, key=lambda c: distance(city, c))
        closest_center_index = random_centers.index(closest_center)
        clusters[closest_center_index].append(city)
    
    return clusters

def create_tour(cluster):
    tour = [0]  # start at the depot
    available_cities = cluster[:]
    current_city = 0
    
    while available_cities:
        next_city = min(available_cities, key=lambda c: distance(current_city, c))
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
        
    tour.append(0)  # go back to the depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

clusters = cluster_cities(num_robots)
tours = {r: create_tour(clusters[r]) for r in range(num_robots)}
tour_costs = {r: calculate_tour_cost(tours[r]) for r in tours}
max_cost = max(tour_costs.values())

# Output the results
for robot_id in tours:
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robotid]}")

print(f"Maximum Travel Cost: {max_cost}")