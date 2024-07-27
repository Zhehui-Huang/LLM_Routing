import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate total distance for a tour
def calculate_total_distance(tour_path):
    total_distance = 0
    for i in range(len(tour_path) - 1):
        total_distance += euclidean(cities[tour_path[i]], cities[tour_path[i + 1]])
    return total_distance

# Generate initial solution + greedy pick
def initial_solution():
    visited = [0]
    while len(visited) < 12:
        last_visited = visited[-1]
        next_city = min((c for c in cities if c not in visited), key=lambda x: euclidean(cities[last_visited], cities[x]))
        visited.append(next_city)
    visited.append(0)  # return to depot
    return visited

# Local optimization: Swap cities in tour
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if calculate_total_distance(new_tour) < calculate_total_distance(tour):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# VNS method for optimization
def variable_neighborhood_search():
    best_tour = initial_solution()
    best_cost = calculate_total_distance(best_tour)
    print(f"Initial Tour Cost: {best_cost}")

    # Continuously optimize by local searches and perturbations
    iterations = 0
    while iterations < 100:
        # Optimize the current tour
        new_tour = optimize_tour(best_tour)
        new_cost = calculate_total_distance(new_tottur)
        print(f"Optimized Tour Cost: {new_cost}")

        # Accept the new tour if it's better
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost
        iterations += 1
    
    return best_tour, best_cost

# Compute the best tour and its cost
final_tour, final_cost = variable_neighborhood_search()

print(f"Tour: {final_tour}")
print(f"Total travel cost: {round(final_cost, 2)}")