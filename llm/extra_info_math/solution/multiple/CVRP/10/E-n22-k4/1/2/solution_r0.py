import numpy as np
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_cities = len(coordinates)
num_robots = 4
robot_capacity = 6000

# Compute the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')

# Vehicle Routing Heuristic
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
current_locations = [0] * num_robots
unvisited_cities = set(range(1, num_cities))

# Assign each city to a robot in a greedy manner (nearest neighbor heuristic)
while unvisited_cities:
    for robot in range(num_robots):
        if not unvisited_cities:
            break
        nearest_city = None
        min_distance = float('inf')
        for city in unvisited_cities:
            if current_loads[robot] + demands[city] <= robot_capacity:
                distance = distance_matrix[current_locations[robot]][city]
                if distance < min_distance:
                    nearest_city = city
                    min_distance = distance
        if nearest_city is not None:
            tours[robot].append(nearest_city)
            current_loads[robot] += demands[nearest_city]
            current_locations[robot] = nearest_city
            unvisited_cities.remove(nearest_city)

# Complete the tours returning to the depot
for robot in range(num_robots):
    tours[robot].insert(0, 0)
    tours[robot].append(0)

# Calculate the travel costs
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

total_costs = [calculate_tour_cost(tour) for tour in tours]
overall_cost = sum(total_costs)

# Output the results
for r, cost in enumerate(total_costs):
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")