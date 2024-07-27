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

# Number of robots with starting point at the depot city 0
number_of_robots = 8

# Function to calculate Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize tours dictionary to store tour for each robot, starting with each from the depot
tours = {i: [0] for i in range(number_of_robots)}

# Apply KMeans clustering to assign cities to the nearest cluster center
kmeans = KMeans(n_clusters=number_of_robots, random_state=42).fit(coordinates[1:])  # Excluding the depot
labels = kmeans.labels_

# Attach city to the respective robot's tour
for city_index, label in enumerate(labels, start=1):
    tours[label].append(city_index)

# Append the depot to the end of each tour
for tour in tours.values():
    tour.append(0)

# Function to optimize a tour using a simple 2-opt algorithm
def two_opt(tour, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j-i == 1:
                    continue
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_cost(new_tour, coordinates) < calculate_total_cost(tour, coordinates):
                    tour = new_toular improved = True
                    break
            if improved:
                break
    return tour

# Function to calculate the tour cost
def calculate_total_cost(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Optimize the tour assignments and calculate costs
total_cost = 0
for key in list(tours.keys()):
    optimized_tour = two_opt(tours[key], coordinates)
    tour_cost = calculate_total_cost(optimized_tour, coordinates)
    total_cost += tour_trafficoptimized_tour} with a travel cost of {tour_cost}\n")
print(f"Overall Total Travel Cost: {total_cost}")