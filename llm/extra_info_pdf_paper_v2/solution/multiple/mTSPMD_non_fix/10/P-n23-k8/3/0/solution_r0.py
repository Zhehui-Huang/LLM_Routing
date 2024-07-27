import random
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Distance calculation function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Simulated Annealing Algorithm Components
def simulated_annealing(cities):
    # Set initial temperature and cooling rate
    temp = 10000
    cooling_rate = 0.995
    current_solution = list(cities.keys())
    random.shuffle(current_solution)
    best_solution = current_solution[:]
    best_cost = tour_cost(best_solution)

    while temp > 1:
        new_solution = current_solution[:]
        # Swap two cities in the tour
        i, j = random.sample(range(len(new_solution)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_cost = tour_cost(new_solution)
        cost_difference = new_cost - tour_cost(current_solution)

        if cost_difference < 0 or random.random() < math.exp(-cost_difference / temp):
            current_solution = new_solution[:]
            if new_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = new_cost
        
        temp *= cooling_rate
    return best_solution, best_cost

# Calculate total travel cost of the tour
def tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

# Solve the problem
best_tour, best_total_cost = simulated_annealing(cities)

# Assign robots to segments of the path
segment_size = len(best_tour) // num_robots
tours = [best_tour[i * segment_size:(i + 1) * segment_size + 1] for i in range(num_robots)]
if len(best_tour) % num_robots:
    tours[-1].extend(best_tour[-(len(best_tour) % num_robots):])

robot_tours_and_costs = [(tour, tour_cost(tour)) for tour in tours]

# Output results
overall_total_cost = sum(cost for _, cost in robot_tours_and_costs)
for robot_id, (tour, cost) in enumerate(robot_tours_and_costs):
    print(f"Robot {robot==>_id} Tour:", tour)
    print(f"Robot {robot_id} Total Travel Cost:", cost)

print("Overall Total Travel Cost:", overall_total_cost)