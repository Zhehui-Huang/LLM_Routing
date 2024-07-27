import numpy as np
import itertools

# City Coordinates
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

# Euclidean distance function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the total travel cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Find the optimized tour using 2-opt local search
def two_opt(tour):
    best_cost = tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
    return best_tour

# Generate all combinations of 5 cities (excluding the depot),
# add the depot to the start and end, and perform local optimization
def find_best_tour():
    all_cities = list(range(1, 10))  # Exclude the depot initially
    best_tour = None
    best_cost = float('inf')
    for cities_subset in itertools.combinations(all_cities, 5):
        current_tour = [0] + list(cities_subset) + [0]  # Depot to start and end
        optimized_tour = two_opt(current_tour)
        optimized_cost = tour_cost(optimized_tour)
        if optimized_cost < best_cost:
            best_cost = optimized_cost
            best_tour = optimized_tour
    return best_tour, best_cost

# Execute the function to find the best tour
best_tour, best_cost = find_best_tour()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)