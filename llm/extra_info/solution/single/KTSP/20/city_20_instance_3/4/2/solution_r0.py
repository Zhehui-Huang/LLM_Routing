import itertools
import math

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Utility to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generates all possible tours given a list of city indices
def find_best_tour_with_fixed_cities(selected_cities):
    best_tour = None
    best_cost = float('inf')
    
    # Starting from depot, loop through each permutation of the other cities
    for perm in itertools.permutations(selected_cities[1:]):
        tour = [0] + list(perm) + [0]
        total_cost = 0
        
        # Calculate total cost of the tour
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(tour[i], tour[i + 1])
        
        # Compare to find the best tour
        if total_cost < best_cost:
            best_cost = total_cost
            best_tour = tour
    
    return best_tour, best_cost

# Main procedure to find the optimal tour of 13 cities
def solve_tsp_with_fixed_cities_count():
    all_cities_except_depot = list(range(1, 20))
    best_global_tour = None
    best_global_cost = float('inf')
    
    # Iterate all combinations of 12 cities (excluding depot)
    for cities_selection in itertools.combinations(all_cities_except_depot, 12):
        selected_cities = [0] + list(cities_selection)
        tour, cost = find_best_tour_with_fixed_cities(selected_cities)
        
        if cost < best_global_cost:
            best_global_cost = cost
            best_global_tour = tour
    
    return best_global_tour, best_global_cost

# Execute the procedure
tour, total_cost = solve_tsp_with_fixed_cities_count()
print("Tour:", tour)
print("Total travel cost:", total_cost)