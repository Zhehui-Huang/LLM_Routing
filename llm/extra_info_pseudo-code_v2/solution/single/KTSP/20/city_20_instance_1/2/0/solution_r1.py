import random
import math

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Euclidean distance calculation
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate total distance of the tour
def tour_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += calc_distance(tour[i], tour[i + 1])
    return total

# Generate a random initial solution of k cities
def generate_initial_solution(k):
    selected = random.sample(list(cities.keys()), k)
    if 0 not in selected:
        selected.pop()
        selected.insert(0, 0)
    selected.append(0)  # To make it a round trip
    return selected

# Local search (simple 2-opt swap)
def local_search(solution):
    best_solution = solution
    best_cost = tour_distance(solution)
    
    for i in range(1, len(solution) - 3):
        for j in range(i + 2, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i:j + 1] = reversed(new_solution[i:j + 1])
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
    
    return best_solution

# GVNS algorithm
def gvns(max_iter=100, k=7):
    best_solution = generate_initial_solution(k)
    best_cost = tour_distance(best_solution)
    
    for _ in range(max_iter):
        current_solution = generate_initial_solution(k)
        current_solution = local_search(current_solution)
        current_cost = tour_distance(current_result)
        
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    
    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))