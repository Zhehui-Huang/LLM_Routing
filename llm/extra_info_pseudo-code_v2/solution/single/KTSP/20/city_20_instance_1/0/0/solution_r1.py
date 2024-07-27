import math
import random

# Define cities coordinates
cities = [
    (14, 77),   # City 0 - Depot
    (34, 20),   # City 1
    (19, 38),   # City 2
    (14, 91),   # City 3
    (68, 98),   # City 4
    (45, 84),   # City 5
    (4, 56),    # City 6
    (54, 82),   # City 7
    (37, 28),   # City 8
    (27, 45),   # City 9
    (90, 85),   # City 10
    (98, 76),   # City 11
    (6, 19),    # City 12
    (26, 29),   # City 13
    (21, 79),   # City 14
    (49, 23),   # City 15
    (78, 76),   # City 16
    (68, 45),   # City 17
    (50, 28),   # City 18
    (69, 9)     # City 19
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Parameters for GVNS algorithm
k = 7
itermax = 100
pmax = 2

# Generate an initial solution with k cities
def generate_initial_solution():
    solution = [0]  # Start at the depot
    while len(solution) < k:
        new_city = random.randint(1, 19)  # Choose from city 1 to 19
        if new_city not in solution:
            solution.append(new_city)
    solution.append(0)  # End at the depot
    return solution

# Shake routine to perturb the solution within the p-th neighborhood
def shake(solution, p):
    idx_to_swap = random.sample(range(1, k-1), 2)  # Avoid the depot at index 0 and last
    solution[idx_to_swap[0]], solution[idx_to_swap[1]] = solution[idx_to_swap[1]], solution[idx_to_swap[0]]
    return solution

# Local search to find an improved solution in the neighborhood
def local_search(solution):
    best_cost = evaluate(solution)
    best_solution = solution[:]
    for i in range(1, k-1):
        for j in range(i+1, k):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_structure[i]
            new_cost = evaluate(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution
    return best_solution

# Evaluate the total travel cost of a tour
def evaluate(solution):
    cost = sum(distance(solution[i], solution[i+1]) for i in range(len(solution)-1))
    return cost

# GVNS algorithm
def GVNS():
    best_solution = generate_initial_solution()
    best_cost = evaluate(best_solution)
    iteration = 0

    while iteration < itermax:
        p = 1
        while p <= pmax:
            shaken_solution = shake(best_solution[:], p)
            new_solution = local_search(shaken_solution)
            new_cost = evaluate(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 1
            else:
                p += 1
        iteration += 1

    return best_solution, best_cost

# Perform the GVNS search
final_tour, final_cost = GVNS()
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")