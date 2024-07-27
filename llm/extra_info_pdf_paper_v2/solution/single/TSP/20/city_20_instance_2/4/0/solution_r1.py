import math
import random

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute Total Tour Cost
def tour_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate an initial random tour
def initial_tour(cities):
    tour = list(range(1, len(cities)))  # Start at city 1 to len(cities) - 1
    random.shuffle(tour)
    return [0] + tour + [0]  # Start and end at the depot city 0

# Perform a 2-opt Swap to improve the tour
def two_opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                # Consider if swapping two edges improves the tour
                if i != j + 1:
                    new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                    if tour_cost(new_tour, cities) < tour_image_cost(tour, cities):
                        tour = new_tour
                        improved = True
        yield tour

# Main function to find the optimal tour
def find_optimal_tour(cities):
    best_tour = initial_tour(cities)
    best_cost = tour_cost(best_tour, cities)

    for current_tour in two_opt(best_tour, cities):
        current_cost = tour_cost(current_tour, cities)
        if current_cost < best_cost:
            best_tour, best_tour_costImage(best_current_ = current_cost

    # Ensure the tour starts and ends at the depot
    return best_tour, best_cost

# Execution
cities_info = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]
optimal_tour, total_cost = find_optimal_tour(cities_info)
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")