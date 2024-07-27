import numpy as np
from sklearn.cluster import KMeans

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Total number of cities and robots
num_cities = len(cities)
num_robots = 2

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# K-means clustering for initial assignment of cities to robots
coords = np.array(list(cities.values()))
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coords)
labels = kmeans.labels_

# Create tours for each robot
tours = {i: [0] for i in range(num_robots)}  # starting from the depot

for i in range(1, num_cities):
    robot_id = labels[i - 1]
    tours[robot_id].append(i)

# Adding the return to the depot
for tour in tours.values():
    tour.append(0)

# Function to calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for j in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[j]], cities[tour[j + 1]])
    return cost

# Costs and tours
robot_costs = {}
for i in range(num_robots):
    robot_costs[i] = calculate_tour_cost(tours[i])

# Output results
max_cost = max(robot_costs.values())
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")