import math
import random

# City coordinates with depot index starting from 0
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def simulated_annealing(T, alpha, num_iterations, cities, num_robots):
    current_solution = list(cities.keys())[2:]  # exclude depots initially
    random.shuffle(current_solution)
    current_solution = [0] + current_solution + [1]  # start at depot city 0, end at depot city 1
    current_cost = tour_cost(current_solution)
    
    for _ in range(num_iterations):
        T *= alpha
        l, r = 1, len(current_solution) - 2  # Don't move depot start and end points
        l, r = sorted(random.sample(range(l, r + 1), 2))
        next_solution = current_solution[:]
        next_solution[l:r+1] = reversed(next_solution[l:r+1])
        next_cost = tour_cost(next_solution)
        
        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / T):
            current_solution, current_cost = next_solution, next_cost

    # Split solution divides the list to assign to robots
    split_point = len(current_solution) // 2
    robot_0_tour = [0] + current_solution[1:split_point]
    robot_1_tour = [0] + current_solution[split_point:]

    return robot_0_tour, robot_1_tour

def tour_cost(solution):
    return sum(distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1))

# Parameters for SA
T = 10000
alpha = 0.995
num_iterations = 10000
num_robots = 2

# Solve the problem using Simulated Annealing
robot_0_tour, robot_1_tour = simulated_annealing(T, alpha, num_iterations, cities, num_robots)

robot_0_cost = tour_cost(robot_0_tour)
robot_1_cost = tour_cost(robot_1_tour)
total_cost = robot_0_cost + robot_1_cost

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", total_cost)