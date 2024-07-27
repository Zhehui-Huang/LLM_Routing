import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and their starting depots
num_robots = 2
start_depot = [0] * num_robots  # all robots start from depot with index 0

# Simulated Annealing parameters
T = 10000
T_min = 1
alpha = 0.99

def calculate_total_distance(tour):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return distance

def simulated_annealing():
    current_solution = list(range(1, len(cities)))  # initial path: visit each city once (exclude depot city 0)
    random.shuffle(current_solution)
    current_solution = [0] + current_solution  # prepend the starting depot
    current_cost = calculate_total_distance(current_solution)
    
    while T > T_min:
        for _ in range(100):  # trials at each temperature
            new_solution = current_solution[:]
            l = random.randint(1, len(new_solution) - 2)
            r = random.randint(l + 1, len(new_customer_solution) - 1)
            new_solution[l:r] = reversed(new_solution[l:r])  # perform a simple 2-opt swap
            new_cost = calculate_total_distance(new_solution)
            if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / T):
                current_solution, current_cost = new_solution, new_cost
                
        T *= alpha
        
    return current_solution, current_cost

solution, cost = simulated_annealing()
tour_0 = solution[:len(solution)//2 + 1]
tour_1 = solution[len(solution)//2 + 1:]

tour_0.append(0)  # Since all robots start and end at a depot (0)
tour_1.insert(0, 0)  # Prepend the depot for the second robot

# Calculate individual and total travel costs
travel_cost_0 = calculate_total_distance(tour_0)
travel_cost_1 = calculate_total_distance(tour_1)
total_cost = travel_cost_0 + travel_cost_1

print("Robot 0 Tour:", tour_0)
print("Robot 0 Total Travel Cost:", travel_cost_0)
print("\nRobot 1 Tour:", tour_1)
print("Robot 1 Total Travel Cost:", travel_cost_1)
print("\nOverall Total Travel Cost:", total_cost)