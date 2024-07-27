import math
import random

# Coordinates of the cities and depots
coordinates = [
    (30, 40), (37, 52), # Depots
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Euclidean distance calculator
def euclidean_distance(idx1, idx2):
    return math.sqrt((coordinates[idx1][0] - coordinates[idx2][0]) ** 2 + (coordinates[idx1][1] - coordinates[idx2][1]) ** 2)

# Initial random assignment of cities to each robot
cities = list(range(2, len(coordinates)))  # Exclude the depots initially
random.shuffle(cities)

mid_index = len(cities) // 2
robot1_cities = [0] + cities[:mid_index]  # Robot 0 starts and ends at depot 0
robot2_cities = [1] + cities[mid_index:]  # Robot 1 starts and ends at depot 1

# Simulated Annealing Setup
def simulated_annealing(robot_cities):
    T = 1000
    Tmin = 1
    alpha = 0.99
    while T > Tmin:
        i = random.randint(1, len(robot_cities) - 2)
        j = random.randint(1, len(robot_cities) - 2)
        if i != j:
            robot_cities[i], robot_cities[j] = robot_cities[j], robot_cities[i]
            new_cost = sum(euclidean_distance(robot_cities[k], robot_cities[k + 1]) for k in range(len(robot_cities) - 1))
            if new_cost < current_cost:
                current_cost = new_cost
            else:
                robot_cities[i], robot_cities[j] = robot_cities[j], robot_cities[i]
        T *= alpha
    return robot_cities, current_cost

current_cost = sum(euclidean_distance(robot1_cities[k], robot1_cities[k + 1]) for k in range(len(robot1_cities) - 1))
robot1_cities, robot1_cost = simulated_annealing(robot1_cities)

current_cost = sum(euclidean_distance(robot2_cities[k], robot2_cities[k + 1]) for k in range(len(robot2_cities) - 1))
robot2_cities, robot2_cost = simulated_annealing(robot2_cities)

# Show results
print(f"Robot 0 Tour: {robot1_cities}")
print(f"Robot 0 Total Travel Cost: {robot1_cost:.2f}\n")

print(f"Robot 1 Tour: {robot2_cities}")
print(f"Robot 1 Total Travel Cost: {robot2_cost:.2f}\n")

print(f"Overall Total Travel Cost: {robot1_cost + robot2_cost:.2f}")