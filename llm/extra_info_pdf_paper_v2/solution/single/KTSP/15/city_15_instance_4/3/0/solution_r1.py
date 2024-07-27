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

# Local optimization: Swap cities in the tour
def optimize_tour(tour):
    best_tour = tour[:]
    best_cost = calculate_total_distance(best_tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_total_distance(new_tour)
            if new_cost < best_cost:  # Find improvement
                best_tour, best_cost = new_tour[:], new_cost
    return best_tour

# Variable Neighborhood Search
def variable_neighborhood_search():
    best_tour = initial_solution()
    best_cost = calculate_total_distance(best_tour)

    improving = True
    while improving:
        new_tour = optimize_tour(best_tour)
        new_cost = calculate_total_distance(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost  # Improved solution found
        else:
            improving = False  # Stop if no improvement
    return best_tour, best_cost

# Execute the search to find an optimal tour
final_tour, total_cost = variable_neighborhood_search()

# Display the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {round(total_cost, 2)}")