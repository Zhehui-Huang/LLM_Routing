import math
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots and their initial depots
num_robots = 2
depots = {0: 0, 1: 1}

# Function to calculate Euclidean distance between two cities
def calc_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Simulated Annealing functions
def initial_solution():
    # Create an initial random solution where each robot gets roughly half the cities
    all_cities = list(cities.keys())[2:]  # Exclude the depot cities from this list
    random.shuffle(all_cities)
    mid_index = len(all_cities) // 2
    robot_tours = {0: [depots[0]] + all_cities[:mid_index], 1: [depots[1]] + all_cities[mid_index:]}
    return robot_tours

def calculate_total_cost(tours):
    total_cost = 0
    tour_costs = []
    for robot_id, tour in tours.items():
        cost = 0
        for i in range(len(tour) - 1):
            cost += calc_distance(tour[i], tour[i+1])
        tour_costs.append(cost)
        total_cost += cost
    return total_cost, tour_costs

def swap_cities(tours):
    # Randomly choose two cities from different robots' tours and swap them
    if len(tours[0]) > 2 and len(tours[1]) > 2:
        swap_idx_1 = random.randint(1, len(tours[0]) - 1)
        swap_idx_2 = random.randint(1, len(tours[1]) - 1)
        tours[0][swap_idx_1], tours[1][swap_idx_2] = tours[1][swap_idx_2], tours[0][swap_idx_1]

def simulated_annealing():
    current_solution = initial_solution()
    current_cost, _ = calculate_total_cost(current_solution)
    temp = 10000
    cooling_rate = 0.995
    while temp > 1:
        new_solution = current_solution.copy()
        new_solution[0] = current_solution[0][:]
        new_solution[1] = current_solution[1][:]
        swap_cities(new_solution)
        new_cost, _ = calculate_total_cost(new_solution)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution = new_solution
            current_cost = new_cost
        temp *= cooling_rate
    return current_solution, current_cost

# Find and print the best solution
best_solution, overall_cost = simulated_annealing()
best_solution_costs = calculate_total_cost(best_solution)[1]

output = []
for robot_id in range(num_robots):
    tour_output = f"Robot {robot_id} Tour: {best_solution[robot_id]}"
    cost_output = f"Robot {robot_id} Total Travel Cost: {best_solution_costs[robot_id]}"
    output.extend([tour_output, cost_output])

output.append(f"Overall Total Travel Cost: {overall_cost}")

for line in output:
    print(line)