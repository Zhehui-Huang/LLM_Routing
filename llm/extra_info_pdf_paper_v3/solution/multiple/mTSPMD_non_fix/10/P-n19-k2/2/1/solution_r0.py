import random
import math
from itertools import permutations

# Cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance calculation utility
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial random solution: Each robot gets a random permutation of all cities excluding depots
def generate_initial_solution():
    all_cities = list(range(2, len(cities)))
    random.shuffle(all_cities)
    mid_point = len(all_cities) // 2
    return all_cities[:mid_point], all_cities[mid_point:]

# Simulated Annealing process
def simulated_annealing(initial_solution):
    current_solution = initial_solution
    current_cost = calculate_solution_cost(current_solution)
    temp = 10000
    temp_min = 0.001
    alpha = 0.995

    while temp > temp_min:
        new_solution = neighbors(current_solution)
        new_cost = calculate_solution_cost(new_solution)
        
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / temp):
            current_solution = new_solution
            current_cost = new_cost
            
        temp *= alpha

    return current_solution, current_cost

# Calculate current solution cost
def calculate_solution_cost(tours):
    cost0 = calculate_tour_cost([0] + tours[0] + [0])
    cost1 = calculate_tour_cost([1] + tours[1] + [1])
    return cost0, cost1, cost0 + cost1

# Calculate individual tour cost, including returning to the start point
def calculate_tour_cost(tour):
    return sum(calculate_distance(cities[tour[i - 1]], cities[tour[i]]) for i in range(1, len(tour)))

# Generate new neighbors of solution
def neighbors(solution):
    tour1, tour2 = solution
    if random.random() > 0.5 and len(tour1) > 1:  # Modify first tour
        i, j = sorted(random.sample(range(len(tour1)), 2))
        tour1[i:j+1] = reversed(tour1[i:j+1])
    else:  # Modify second tour
        i, j = sorted(random.sample(range(len(tour2)), 2))
        tour2[i:j+1] = reversed(tour2[i:j+1])
    return (tour1, tour2)

# Main execution
initial_solution = generate_initial_solution()
optimized_solution, optimzied_cost = simulated_annealing(initial_solution)
cost0, cost1, total_cost = calculate_solution_cost(optimized_solution)

# Output
print(f"Robot 0 Tour: {[0] + optimized_solution[0] + [0]}")
print(f"Robot 0 Total Travel Cost: {cost0}")
print(f"Robot 1 Tour: {[1] + optimized_solution[1] + [1]}")
print(f"Robot 1 Total Travel Cost: {cost1}")
print(f"Overall Total Travel Cost: {total_cost}")