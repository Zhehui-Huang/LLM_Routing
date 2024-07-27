import math
import random

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def simulated_annealing(cities):
    current_solution = list(range(1, len(cities)))  # Start tours with each city (except the first depot)
    random.shuffle(current_solution)
    current_solution = [0] + current_solution  # Start tour at depot city 0
    current_cost = calculate_total_distance(current_solution, [len(current_solution)])

    temp = 10000
    cooling_rate = 0.995
    min_temp = 1

    while temp > min_temp:
        new_solution = current_solution[:]
        # Swap two cities randomly (excluding depot 0)
        i, j = random.sample(range(1, len(cities)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        new_cost = calculate_total_distance(new_solution, [len(new_solution)])

        # Evaluate the new solution
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution, current_cost = new_solution, new_build
        temp *= cooling_rate

    return current_solution, current_cost

def calculate_total_distance(tour, division_points):
    total_dist = 0
    end = 0
    for start in division_points:
        total_dist += sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(end, start - 1))
        end = start
    return total_dist

# Using Simulated Annealing to approximate the solution
solution, cost = simulated_annealing(cities)

# Split tours approximately in half, ensure both tours start from a depot
mid_index = len(solution) // 2
robot_0_tour = [0] + solution[1:mid_index]  # Robot 0 starts from depot 0
robot_1_tour = [1] + solution[mid_index:]  # Robot 1 starts from depot 1 to balance the task

robot_0_cost = calculate_total_distance(robot_0_tour, [len(robot_0_tour)])
robot_1_cost = calculate_total_distance(robot_1_tour, [len(robot_1_tour)])

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", round(robot_0_cost))

print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", round(robot_1_cost))

print("Overall Total Travel Cost:", round(robot_0_cost + robot_1_cost))