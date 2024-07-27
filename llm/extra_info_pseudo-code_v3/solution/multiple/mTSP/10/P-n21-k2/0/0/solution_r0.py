import numpy as np
import math
from sklearn.cluster import KMeans

# City coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    c1, c2 = coordinates[city1], coordinates[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Number of robots
num_robots = 2

# Cluster cities (excluding the depot) using k-means
city_locations = np.array([coordinates[i] for i in range(1, 21)])
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locations)
labels = kmeans.labels_

# Create initial tours
tours = {i: [0] for i in range(num_robots)}
for i, label in enumerate(labels):
    tours[label].append(i + 1)

# Complete the tour by returning to the starting city
for tour in tours.values():
    tour.append(0)

# Calculate the travel cost for each tour
def calc_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Print tours and costs
overall_total_cost = 0
for i in range(num_robots):
    tour_cost = calc_tour_cost(tours[i])
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")