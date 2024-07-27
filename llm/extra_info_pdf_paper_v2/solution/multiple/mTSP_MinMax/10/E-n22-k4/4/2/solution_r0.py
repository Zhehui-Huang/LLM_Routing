import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Sorting cities to facilitate clustering
sorted_cities_index = sorted(cities.keys(), key=lambda k: (cities[k][0], cities[k][1]))
sorted_cities_index.remove(0)  # Remove the depot from sorting (it remains as the starting point)

# Assign cities to robots
num_robots = 4
robot_tours = {i: [0] for i in range(num_robots)}  # Initialize tours starting at the depot

# Fairly distribute cities to each robot
size = len(sorted_cities_index) // num_robots
for i in range(num_robots):
    if i == num_robots - 1:
        # Assign remaining cities to last robot
        robot_tours[i] += sorted_cities_index[i*size:]
    else:
        robot_tours[i] += sorted_cities_index[i*size:(i+1)*size]
    robot_tours[i].append(0)  # Ending at the depot city

# Calculate the travel cost for each tour and find the max cost
max_travel_cost = 0
for robot, tour in robot_tours.items():
    cost = 0
    for j in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[j-1]], cities[tour[j]])
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(cost, 2)}")
    max_travel_cost = max(max_travel_cost, cost)

print(f"Maximum Travel Cost: {round(max_travel_cost, 2)}")