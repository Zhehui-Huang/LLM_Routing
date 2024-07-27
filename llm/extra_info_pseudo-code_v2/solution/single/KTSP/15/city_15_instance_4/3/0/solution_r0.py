import random
import math

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Euclidean distance calculator
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating initial solution
def generate_initial_solution(k):
    keys = list(cities.keys())
    random.shuffle(keys)
    # Ensure depot city is in the tour
    if 0 not in keys[:k]:
        keys.remove(0)
        keys.insert(random.randint(0, k-1), 0)
    return keys[:k]

# Calculate total cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    # Return to the starting city
    total_cost += distance(tour[-1], tour[0])
    return total_cost

# Local search operation - swap cities to find a better tour
def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_cost(tour)
    n = len(tour)
    for i in range(n):
        for j in range(i + 1, n):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
    return best_tour

# Main GVNS function
def gvns(k, max_iter=1000):
    best_tour = generate_initial_solution(k)
    best_cost = calculate_cost(best_tour)
    iter_count = 0
    while iter_count < max_iter:
        current_tour = generate_initial_solution(k)
        current_tour = local_search(current_tour)
        current_cost = calculate_cost(current_tour)
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost
        iter_count += 1
    return best_tour, best_cost

# Constants
K = 12  # We need 12 cities including the depot city
MAX_ITER = 5000

# Solve the problem
final_tour, final_cost = gvns(K, MAX_ITER)
final_tour.append(0)  # Append the depot city to complete the tour

# Output
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))