import numpy as np
from itertools import permutations

# Given city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Euclidean distance calculator
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate random subset of cities including the depot
def select_cities(num_cities, total_cities):
    selected = np.random.choice(range(1, total_cities), num_cities - 1, replace=False).tolist()
    selected.insert(0, 0)  # always include the depot as the start and end
    selected.append(0)  # end at the depot
    return selected

# Calculate total travel cost for the tour
def tour_cost(tour, city_coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return total_cost

# Perform exhaustive search on a smaller space
def find_best_tour(cities_subset, city_coords):
    subset_coords = [city_coords[i] for i in cities_subset]
    min_tour = None
    min_cost = float('inf')
    for perm in permutations(subset_coords):
        current_tour = list(perm)
        current_tour.insert(0, city_coords[0])  # start at depot
        current_tour.append(city_coords[0])  # end at depot
        cost = tour_cost(current_tour, city_coords)
        if cost < min_cost:
            min_cost = cost
            min_tour = [city_coords.index(x) for x in current_tour]
    return min_tour, min_cost

# Main heuristic solver
def solve_k_tsp(city_coords, num_cities, iterations=1000):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(iterations):
        cities_subset = select_cities(num_cities, len(city_coords))
        current_tour, current_cost = find_best_tour(cities_subset, city_coords)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Required to visit 16 cities starting and ending at city 0
tour, cost = solve_k_tsp(cities, 16)
print("Tour:", tour)
print("Total travel cost:", cost)