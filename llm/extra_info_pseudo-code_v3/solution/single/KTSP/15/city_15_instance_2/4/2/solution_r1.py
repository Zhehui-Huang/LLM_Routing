import random
import math

# Coordinates for the cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculation of the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generates a random initial solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 7) + [0]
    return tour

# Total length of the tour
def tour_length(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to perform the neighborhood search
def variable_neighborhood_descent(solution):
    best_solution = solution[:]
    best_cost = tour_length(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, 8):
            for j in range(i + 1, 8):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = tour_length(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
    return best_solution, best_cost

# GVNS algorithm
def GVNS(restarts):
    best_cost = float('inf')
    best_solution = None

    for _ in range(restarts):
        initial_solution = generate_initial_solution()
        solution, cost = variable_neighborhood_descent(initial_solution)
        for _ in range(10):  # Number of shakes
            # Shake by swapping two random cities in the tour
            idx1, idx2 = random.sample(range(1, 8), 2)
            solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
            solution, cost = variable_neighborhood_descent(solution)
            if cost < best_cost:
                best_solution, best_cost = solution, cost
    return best_solution, best_cost

# Running the GVNS
best_tour, best_cost = GVNS(100)

# Output the resulting tour and the associated total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")