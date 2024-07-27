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

def simulated_annealing(cities):
    curr_solution = list(range(2, len(cities)))  # start from city 2 since 0 and 1 are depots
    random.shuffle(curr_solution)
    curr_solution = [0] + curr_solution  # starting at depot for robot 0
    curr_cost = total_distance(curr_solution)

    temp = 10000
    cooling_rate = 0.995
    min_temp = 1

    while temp > min_temp:
        i, j = random.sample(range(1, len(curr_solution)), 2)  # sample two indices, ensuring not to include the depot
        new_solution = curr_solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        
        new_cost = total_distance(new_solution)
        if new_cost < curr_cost or random.random() < math.exp((curr_cost - new_cost) / temp):
            curr_solution, curr_cost = new_solution, new_cost

        temp *= cooling_rate

    return curr_solution, curr_cost

def total_distance(solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += euclidean_distance(cities[solution[i]], cities[solution[i + 1]])
    return distance

# Simulated Annealing to find a solution
tour, tour_cost = simulated_annealing(cities)

# Decision to split the single tour into two for the robots
# Distribute cities approximately equally
mid_point = len(tour) // 2
robot_0_tour = [0] + tour[1:mid_point]
robot_1_tour = [1] + tour[mid_point:]

robot_0_cost = total_distance([0] + robot_0_tour + [0])
robot_1_cost = total_distance([1] + robot_1_tour + [1])

# Output results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", round(robot_0_cost))

print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", round(robot_1_cost))

print("Overall Total Travel Cost:", round(robot_0_cost + robot_1_cost))