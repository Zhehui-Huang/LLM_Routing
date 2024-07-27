import math
from itertools import combinations

# City coordinates and demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700
]

# Parameters
num_robots = 4
robot_capacity = 6000

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Initialize tours and robot loads
tours = [[] for _ in range(num_robots)]
robot_loads = [0] * num_robots

# Assign each city to a robot while considering capacity constraints
for i in range(1, len(cities)):
    # Find a robot with the remaining capacity that is closest to city i
    min_additional_cost = float('inf')
    best_robot = None
    best_position = None

    for k in range(num_robots):
        if robot_loads[k] + demands[i] <= robot_capacity:
            # Check all positions in the tour of robot k
            for pos in range(len(tours[k]) + 1):
                # Test insertion between positions in the existing tour
                if pos == 0 and not tours[k]:
                    # Adding the first city to an empty tour
                    tentative_tour = [0, i, 0]
                    additional_cost = 2 * euclidean_distance(0, i)
                else:
                    prev_city = tours[k][pos - 1] if pos > 0 else 0
                    next_city = tours[k][pos] if pos < len(tours[k]) else 0
                    if prev_city == 0 and next_city == 0:
                        continue  # Do not consider appending between two depots
                    cost_without_i = euclidean_distance(prev_city, next_city)
                    cost_with_i = euclidean_distance(prev_city, i) + euclidean_distance(i, next_city)
                    additional_cost = cost_with_i - cost_without_i

                if additional_cost < min_additional_cost:
                    min_additional_cost = additional_cost
                    best_robot = k
                    best_position = pos

    # Assign city i to the best robot at the best insertion position found
    tours[best_robot].insert(best_position, i)
    robot_loads[best_robot] += demands[i]

# Complete the tours with the depot
for t in tours:
    if t:  # There might be empty tours if there are fewer cities than robots
        if t[0] != 0: t.insert(0, 0)
        if t[-1] != 0: t.append(0)

# Compute and print the result
total_cost = 0
for i, tour in enumerate(tours):
    cost = calculate_route_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")