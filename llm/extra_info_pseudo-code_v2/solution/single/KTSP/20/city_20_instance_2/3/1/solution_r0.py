import random
import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 
    18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution
def generate_initial_solution():
    selected = set([0])
    solution = [0]
    while len(solution) < 10:
        remaining = list(set(cities.keys()) - selected)
        next_city = random.choice(remaining)
        solution.append(next_city)
        selected.add(next_city)
    solution.append(0)  # Return to the depot
    return solution

# Calculate total travel cost for a given tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Variable Neighborhood Search
def vns(max_iter=1000, neighborhood_size=20):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(max_iter):
        # Shaking step
        for p in range(1, neighborhood_size + 1):
            # Apply a shake by swapping two random cities (not the depot)
            perturbed_solution = best_solution[:]
            idx1, idx2 = random.sample(range(1, 10), 2)  # Avoid index 0 and last index
            perturbed_solution[idx1], perturbed_solution[idx2] = perturbed_solution[idx2], perturbed_solution[idx1]
            new_cost = calculate_def(perturbed_solution)
            if new_cost < best_cost:
                best_solution = perturbed_solution
                best_cost = new_cost
                
    return best_solution, best_cost

# Execute VNS to find an optimal route
solution, total_cost = vns(max_iter=1000, neighborhood_size=20)
print("Tour:", solution)
print("Total travel cost:", total_cost)