import random
import math

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate the total distance of the tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial solution with random k cities including the depot
def generate_initial_solution(depot, k, total_cities):
    selected_cities = random.sample(range(1, total_cities), k - 1)  # sample without the depot
    tour = [depot] + selected_cities + [depot]
    return tour

# Perform local search to optimize the tour
def local_search(tour):
    best_distance = tour_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_distance = tour_distance(new_tour)
                if new_distance < best_distance:
                    tour, best_distance = new_tour, new_distance
                    improved = True
    return tour, best_distance

# Find the optimal tour
def find_optimal_tour():
    k = 10  # Number of cities to visit including the depot
    total_cities = 20
    depot = 0
    best_tour, best_cost = None, float('inf')

    # Try multiple initial solutions
    for _ in range(100):
        initial_tour = generate_initial_solution(depot, k, total_cities)
        optimized_tour, optimized_cost = local_search(initial_tour)
        if optimized_cost < best_cost:
            best_tour, best_cost = optimized_tour, optimized_cost
    return best_tour, best_cost

# Main execution
best_tour, best_cost = find_optimal_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))