import numpy as np
import random

# Provided data set of cities with positions
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

k = 13  # Number of cities to visit including the depot
itermax = 100
pmax = 2

def euclidean_distance(city_a, city_b):
    return np.sqrt((city_coordinates[city_a][0] - city_coordinates[city_b][0]) ** 2 + 
                   (city_coordinates[city_a][1] - city_coordinates[city_b][1]) ** 2)

def generate_initial_solution():
    available_cities = list(city_coordinates.keys())
    random.shuffle(available_cities)
    S = [0] + available_cities[1:k-1] + [0]
    return S

def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def shake(solution, level):
    new_solution = solution[1:-1]
    if level == 1:
        i, j = random.sample(range(len(new_solution)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    elif level == 2:
        i, j = sorted(random.sample(range(len(new_solution)), 2))
        new_solution[i:j] = reversed(new_solution[i:j])
    return [0] + new_solution + [0]

def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_cost(solution)
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
    return best_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(itermax):
        for _ in range(pmax):
            shaken_solution = shake(best_solution, random.randint(1, 2))
            local_opt_solution = local_search(shaken_solution)
            local_opt_cost = calculate_cost(local_opt_solution)
            if local_opt_cost < best_cost:
                best_solution = local_opt_solution[:]
                best_cost = local_opt_cost

    return best_solution, best_cost

# Running the GVNS algorithm to find the optimal tour
best_tour, total_cost = gvns()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")