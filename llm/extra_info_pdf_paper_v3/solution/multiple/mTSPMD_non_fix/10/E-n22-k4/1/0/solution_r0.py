import math
from random import randint, shuffle
import copy

def euclidean_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def total_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def simulated_annealing(cities, init_temp, min_temp, alpha):
    def get_neighborhood(solution):
        l = len(solution)
        i, j = randint(0, l - 1), randint(0, l - 1)
        solution[i], solution[j] = solution[j], solution[i]
        return solution

    current_solution = list(range(1, len(cities)))  # skip depot at index 0 initially
    shuffle(current_solution)
    current_solution = [0] + current_solution  # start from depot
    current_cost = total_tour_cost(current_solution, cities)
    best_solution = current_solution.copy()
    best_cost = current_cost

    temperature = init_temp

    while temperature > min_temp:
        next_solution = get_neighborhood(current_solution[:])
        next_cost = total_tour_cost(next_solution, cities)

        cost_diff = next_cost - current_cost

        if cost_diff < 0 or math.exp(-cost_diff / temperature) > randint(0, 100) / 100:
            current_solution, current_cost = next_solution, next_cost

            if current_cost < best_cost:
                best_solution, best_cost = current_solution.copy(), current_cost

        temperature *= alpha

    return best_solution, best_cost

# Cities and their coordinates set up
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Parameters
initial_temperature = 100
minimum_temperature = 0.01
alpha = 0.99
num_robots = 4

# Apply the Simulated Annealing algorithm to find an optimal solution
solution, cost = simulated_annealing(cities, initial_temperature, minimum_temperature, alpha)

# Placeholder to break down solution among robots, this needs a more rigorous approach
parts = len(solution) // num_robots  
tours = [solution[i:i + parts + 1] for i in range(0, len(solution), parts)]
tours = [tour + [tour[0]] for tour in tours][:num_robots]  # ensure each tour is a cycle, only feasible for demonstration

# Calculate costs for each tour
tour_costs = [total_tour_cost(tour, cities) for tour in tours]

# Output results
overall_travel_cost = sum(tour_costs)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {overall_travel_cost}")