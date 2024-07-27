import math
import random

# Configuration for simulated annealing
temp_start = 10000
cooling_rate = 0.995
min_temp = 1

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Initial tour divisions (simple split by index)
# robot 0 starts at city 0 and robot 1 starts at city 1
robot_0_tour = [0] + random.sample(range(2, 11), 9)
robot_1_tour = [1] + random.sample(range(11, 21), 10)

# Simulated annealing implementation for TSP
def simulated_annealing(tour):
    current_temp = temp_start
    current_tour = tour[:]
    current_cost = total_cost(current_tour)
    while current_temp > min_temp:
        # Swap two cities in the tour randomly excluding the first city (depot)
        i, j = sorted(random.sample(range(1, len(tour)), 2))
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        new_cost = total_cost(new_tour)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temp):
            current_tour, current_cost = new_tour, new_cost
        current_temp *= cooling_rate
    return current_tour, current_cost

# Obtain optimized tours
optimized_robot_0_tour, robot_0_cost = simulated_annealing(robot_0_tour + [0])
optimized_robot_1_tour, robot_1_cost = simulated_annealing(robot_1_tour + [1])

# Presenting the results
print(f"Robot 0 Tour: {optimized_robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}\n")
print(f"Robot 1 Tour: {optimized_robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}\n")

# Calculate total cost
overall_total_cost = robot_0_cost + robot_1_cost
print(f"Overall Total Travel Cost: {overall_total_cost}")