import numpy as np
import itertools

# Define city coordinates and groupings
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

def euclidean_dist(a, b):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Distance Matrix Calculation
def calculate_distance_matrix():
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean_dist(cities[i], cities[j])
    return dist_matrix

dist_matrix = calculate_distance_matrix()

# Heuristic Solution: 
# I will implement a simple approach to construct an initial valid tour and then try to improve it slightly by local optimization.
def construct_initial_tour():
    chosen_cities = [0]  # Start at the depot
    used_groups = set()
    
    for group in groups:
        min_dist = float('inf')
        selected_city = None
        for city in group:
            if city not in used_groups:
                dist = dist_matrix[chosen_cities[-1]][city]
                if dist < min_dist:
                    min_dist = dist
                    selected_city = city
        chosen_cities.append(selected_city)
        used_groups.add(selected_city)

    chosen_cities.append(0)  # Return to depot
    return chosen_cities

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i - 1]][tour[i]]
    return total_cost

def two_opt_swap(tour, i, k):
    new_tour = tour[0:i] + tour[i:k + 1][::-1] + tour[k + 1:]
    return new_tour

def local_optimization(tour):
    improvement = True
    best_tour = tour
    best_cost = calculate_tour_cost(tour)
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 2, len(tour) - 1):
                new_tour = two_opt_swap(tour, i, k)
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improvement = True
        tour = best_tour
    return tour, best_cost

initial_tour = construct_initial_tour()
optimized_tour, total_cost = local_optimization(initial_tour)

output_tour = [c for c in optimized_tour]  # Ensuring to start and end at depot
output_cost = total_cost

print("Tour:", output_tour)
print("Total travel cost:", round(output_cost, 2))