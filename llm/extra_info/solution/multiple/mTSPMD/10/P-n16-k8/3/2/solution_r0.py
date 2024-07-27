import numpy as np
from scipy.spatial import distance_matrix

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and their starting positions
num_robots = 8
robots = {i: i for i in range(num_robots)}  # robot_id to depot_city_id mapping

# Calculate Euclidean distance matrix
coordinates = np.array(list(cities.values()))
dist_matrix = distance_matrix(coordinates, coordinates)

# Function to calculate the total distance of a path
def calculate_path_distance(path):
    return sum(dist_matrix[path[i], path[i+1]] for i in range(len(path)-1))

# Greedy initial assignment of cities to robots based on closest depot
visits = {i: [i] for i in range(num_robots)}  # each robot starts with its depot city

for city in range(num_robots, len(cities)):
    # Assign city to closest robot depot
    closest_depot = min(range(num_robots), key=lambda x: dist_matrix[city, x])
    visits[closest_depot].append(city)

# Ensure each tour is a circuit: back to the depot
for robot in visits:
    visits[robot].append(visits[robot][0])  # end where it started

# Calculate travel costs for each robot and overall
total_costs = []
for robot, tour in visits.items():
    cost = calculate_path_distance(tour)
    total_costs.append(cost)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

# Calculate and print the overall cost
overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_cost:.2f}")