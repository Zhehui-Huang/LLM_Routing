import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Number of robots
num_robots = 2

# Extract coordinates and city indices
coordinates = np.array(list(cities.values()))
city_indices = np.array(list(cities.keys()))

# Exclude the depot when clustering
non_depot_indices = city_indices[1:]
non_depot_coords = coordinates[1:]

# Use KMeans to cluster cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(non_depot_coords)
labels = kmeans.labels_
grouped_cities = {i: [] for i in range(num_robots)}
for idx, label in enumerate(labels):
    grouped_cities[label].append(non_depot_indices[idx])

# Function to compute the travel cost of a tour
def compute_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

# Simple Nearest Neighbor heuristic to create initial tours for each robot
def create_tour(start_city, cities):
    remaining_cities = set(cities)
    tour = [start_city]
    current_city = start_city
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean(coordinates[current_city], coordinates[x]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
        
    tour.append(start_city) # back to depot
    return tour

robot_tours = {}
overall_cost = 0

# Generate initial tours for each robot
for robot in range(num_robots):
    tour = create_tour(0, grouped_cities[robot])
    tour_cost = compute_tour_cost(tour)
    overall_cost += tour_cost
    robot_tours[robot] = {
        'tour': tour,
        'cost': tour_cost
    }

# Output each robot's tours and costs
for robot, data in robot_tours.items():
    print(f"Robot {robot} Tour: {data['tour']}")
    print(f"Robot {robot} Total Travel Cost: {data['cost']}")

print(f"Overall Total Travel Cost: {overall_cost}")