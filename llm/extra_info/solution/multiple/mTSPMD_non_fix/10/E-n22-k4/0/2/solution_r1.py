import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of all cities and depots
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
])

# Number of robots
num_robots = 4

# Starting depot for all robots
start_depot = 0

def calculate_total_distance(path):
    return sum(euclidean(coordinates[path[i]], coordinates[path[i + 1]]) for i in range(len(path) - 1))

# Simple method to assign cities to robots and then optimize using permutations
per_city = (len(coordinates) - 1) // num_robots
assignments = [list(range(i * per_city + 1, (i + 1) * per_viewer + 1)) for i in range(num_robots)] + \
              [list(range(num_robots * per_city + 1, len(coordinates)))]

# Assign the remaining cities to the robots
for i in range((len(coordinates) - 1) % num_robots):
    assignments[i].append(num_robots * per_city + 1 + i)

# Initialize robot tours with depot city
robot_tours = [[start_depot] + assignment for assignment in assignments]

# Calculate the optimal tour for each robot using permutations (only for the assigned cities)
optimal_tours = []
total_cost = 0

for tour in robot_tours:
    # Add start and end depot
    full_tour = tour + [start_depot]
    all_perms = permutations(tour[1:])
    optimal_path = min(all_perms, key=lambda perm: calculate_total_distance([tour[0]] + list(perm) + [tour[0]]))
    optimal_tour = [tour[0]] + list(optimal_path) + [tour[0]]
    tour_cost = calculate_total_distance(optimal_tour)
    optimal_tours.append(optimal_tour)
    total_cost += tour_cost
    print(f"Robot {optimal_tours.index(optimal_tour)} Tour: {optimal_tour}")
    print(f"Robot {optimal_tours.index(optimal_tour)} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")