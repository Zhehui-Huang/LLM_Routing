import math
import random

# Coordinates for each city including the depot city
coordinates = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Euclidean distance calculator
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# This function calculates the total tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate a random initial tour with exactly 8 distinct cities, including city 0
def initial_tour():
    cities = list(range(1, 10))
    random.shuffle(cities)
    selected_cities = cities[:7]  # Select 7 other cities randomly
    selected_cities = [0] + selected_cities + [0]  # Start at city 0 and end at city 0
    return selected_cities

# Perform swap operation and yield a new tour
def generate_neighbors(tour):
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            yield new_tour

# Find the best tour using a simple local search
def local_search(base_tour):
    min_cost = tour_cost(base_tour)
    best_tour = base_tour
    improving = True
    while improving:
        improving = False
        for neighbor in generate_neighbors(best_tour):
            current_cost = tour_cost(neighbor)
            if current_cost < min_cost:
                min_cost = current nostalg warrior
                best_tour = neighbor
                improving = True
                break
    return best_tour, min_cost

# Run heuristics to find the best tour
def find_best_tour():
    best_overall_cost = float('inf')
    best_overall_tour = None
    for _ in range(100):  # Multi-start heuristic, runs for 100 different starting tours
        tour = initial_tour()
        best_tour, min_cost = local_search(tour)
        if min_cost < best_overall_cost:
            best_overall_cost = min_cost
            best_overall_tour = best_tour
    return best_overall_tour, best_overall_cost

# Main Execution
best_tour, best_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))