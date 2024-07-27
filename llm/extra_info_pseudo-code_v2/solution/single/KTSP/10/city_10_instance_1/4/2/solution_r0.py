import math
import random

# Define cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Distance function (Euclidean)
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the cost of a tour
def evaluate(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Generate an initial random solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 4) + [0]
    return tour

# Shake operation to generate neighboring solution
def shake(tour, degree):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    return [0] + new_tour + [0]

# Local search operation
def local_search(tour):
    best_tour = tour[:]
    best_cost = evaluate(tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = evaluate(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improved = True
    return best_tour

# GVNS Algorithm
def gvns(k=5, itermax=100):
    best_solution = generate_initial_solution()
    best_cost = evaluate(best_solution)
    
    for _ in range(itermax):
        for p in range(1, 4):  # Define pmax as arbitrary 3 for simplicity
            current_solution = shake(best_solution, p)
            local_optimum = local_search(current_solution)
            local_optimum_cost = evaluate(local_optimum)
            
            if local_optimum_cost < best_cost:
                best_solution, best_cost = local_optimum[:], local_optimum_cost

    return best_solution, best_cost

# Running GVNS
final_tour, total_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", total_cost)