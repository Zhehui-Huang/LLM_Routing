import math
import random

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(cities):
    current_solution = list(range(2, len(cities)))  # omit depots initially
    random.shuffle(current_solution)
    current_solution = [0, 1] + current_matrix  # prepend depots
    current_cost = total_distance(current_solution)

    temp = 100
    cooling_rate = 0.995
    min_temp = 1

    while temp > min_temp:
        new_solution = current_solution[:]
        # Swap two cities randomly excluding the first two depots
        i, j = random.sample(range(2, len(cities)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        new_cost = total_distance(new_solution)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution, current_cost = new_solution, new_cost

        temp *= cooling_rate

    return current_solution, current_cost

# Solve the problem using Simulated Annealing
solution, cost = simulated_annealing(cities)

# Split the tour between the two robots, starting after the initial depots
mid_index = len(solution) // 2
robot_0_tour = [0] + solution[2:mid_index] + [solution[1]]
robot_1_tour = [1] + solution[mid_index:]

robot_0_cost = total_distance(robot_0_tour)
robot_1_cost = total_distance(robot_1_tour)

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", round(robot_0_cost))

print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", round(robot_1_cost))

print("Overall Total Travel Cost:", round(robot_0_cost + robot_1_cost))