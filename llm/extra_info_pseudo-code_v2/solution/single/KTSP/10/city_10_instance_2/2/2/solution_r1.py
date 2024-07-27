import math
import random

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to compute the total travel cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate initial feasible solution
def generate_initial_solution(k=6):
    solution = [0]  # start at the depot city
    while len(solution) < k:
        new_city = random.choice([c for c in cities if c not in solution])
        solution.append(new_city)
    solution.append(0)  # return to depot
    return solution

# Shake function to diversify the solutions
def shake(solution, k=2):
    new_solution = solution[:]
    for _ in range(k):
        a, b = random.sample(range(1, len(solution)-2), 2)
        new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
    return new_solution

# Local search to improve the solution
def local_search(solution):
    best_cost = tour_cost(solution)
    best_solution = solution[:]
    for i in range(1, len(solution) - 3):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

# Main GVNS function
def gvns(max_iterations=100, k=6):
    best_solution = generate_initial_solution(k)
    best_cost = tour_cost(best_solution)
    for _ in range(max_iterations):
        current_solution = shake(best_solution)
        improved_solution = local_search(current_solution)
        improved_cost = tour_cost(improved_service)
        if improved_cost) < best_cost:
            best_solution = improved_solution
            best_cost = improved_cost
    return best_solution, best_cost

# Execute GVNS
final_solution, final_cost = gvns()
print("Tour:", final_solution)
print("Total travel cost:", format(final_cost, ".2f"))