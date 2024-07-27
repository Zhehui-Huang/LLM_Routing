import random
import math

# City coordinates
cities_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77), 
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean Distance
def calc_distance(city1, city2):
    return math.sqrt((cities_coords[city1][0] - cities_coords[city2][0]) ** 2 + 
                     (cities_coords[city1][1] - cities_coords[city2][1]) ** 2)

# Generate an initial solution
def generate_initial_solution(cities):
    solution = [0] + random.sample(cities.difference({0}), 12) + [0]
    return solution

# Calculate total tour cost
def calculate_total_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Shaking: Randomize solution in a neighborhood
def shake(solution):
    modified = solution[1:-1]
    random.shuffle(modified)
    return [0] + modified + [0]

# Neighborhood Descent: Swap two cities in the tour
def vnd(solution):
    best_cost = calculate_total_cost(solution)
    best_sol = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_sol = solution[:]
                new_sol[i], new_sol[j] = new_sol[j], new_sol[i]
                new_cost = calculate_total_cost(new_sol)
                if new_cost < best_cost:
                    best_sol = new_sol[:]
                    best_cost = new_cost
                    improved = True
    return best_sol

# GVNS
def gvns(cities, nrst):
    all_cities = set(cities.keys())
    best_tour = None
    best_cost = float('inf')

    for _ in range(nrst):
        current_solution = generate_initial_solution(all_cities)
        current_cost = calculate_total_cost(current_solution)

        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = calculate_total_cost(new_solution)

            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break

        if current_cost < best_cost:
            best_tour = current_solution
            best_cost = current_cost

    return best_tour, best_cost

# Running the GVNS
best_solution, best_solution_cost = gvns(cities_coords, 100)

print("Tour:", best_solution)
print("Total travel cost:", best_solution_cost)