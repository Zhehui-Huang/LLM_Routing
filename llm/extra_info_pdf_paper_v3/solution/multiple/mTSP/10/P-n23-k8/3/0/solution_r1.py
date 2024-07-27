import math
import numpy as np
from sklearn.cluster import KMeans

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Number of robots and starting at depot
number_of_robots = 8

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate total tour cost
def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

# Split tours using clustering based on geographic location
kmeans = KMeans(n_clusters=number_of_robots).fit(coordinates[1:])  # Excluding depot
labels = kmeans.labels_

# Initialize tours for each robot
tours = {i: [0] for i in range(number_of_robots)}  # Start at the depot

# Distributing cities to the closest robot's route
for idx, label in enumerate(labels, start=1):
    tours[label].append(idx)

# Closing each route at the depot city
for tour in tours.values():
    tour.append(0)  # End at the depot

# Apply local optimization for each tour using 2-opt algorithm
def two_opt(tour, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_cost(new_tour, coordinates) < calculate_total_cost(tour, coordinates):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

optimized_tours = {}
for robot_id, tour in tours.items():
    optimized_tours[robot_id] = two_opt(tour, coordinates)

# Display the results
overall_total_cost = 0
for robot_id, tour in optimized_tours.items():
    tour_cost = calculate_total_cost(tour, coordinates)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_totalš_cost:.2f}")