import math
import random

# Define the cities based on given coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15),
}

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate an initial solution
def generate_initial_solution():
    chosen = random.sample(list(cities.keys())[1:], 3)  # Exclude the depot initially
    return [0] + chosen

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    total_cost += distance(tour[-1], tour[0])  # Return to the depot
    return total_cost

# Perform the Shaking step: Create a new solution by small changes
def shake(tour):
    new_tour = tour[:]
    idx_to_change = random.sample(range(1, 4), 2)  # Only change inner cities
    new_tour[idx_to_change[0]], new_tour[idx_to_change[1]] = new_tour[idx_to_change[1]], new_tour[idx_to_change[0]]
    return new_tour

# Variable Neighborhood Descent
def vnd(tour):
    best_tour = tour[:]
    best_cost = calculate_cost(best_tour)
    improved = True
    
    while improved:
        improved = False
        # Try exchanging any pair of cities
        for i in range(1, 4):
            for j in range(i + 1, 4):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
    
    return best_tour

# General Variable Neighborhood Search
def gvns(Nrst=100):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        current_cost = calculate_cost(current_solution)
        
        while True:
            shaken_solution = shake(current_solution)
            new_solution = vnd(shaken_solution)
            new_cost = calculate_cost(new_solution)
            
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
            
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Performing the search
best_tour, total_cost = gvns()
best_tour_complete = best_tour + [best_tour[0]]

# Output
print(f"Tour: {best_tour_complete}")
print(f"Total travel cost: {total_cost}")