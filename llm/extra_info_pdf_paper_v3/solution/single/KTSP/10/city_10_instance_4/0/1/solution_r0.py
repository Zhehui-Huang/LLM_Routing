import itertools
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def evaluate_tour(tour, cities):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    return total_distance

def find_optimal_k_tsp_tour(cities, k):
    city_indices = list(range(len(cities)))
    possible_tours = itertools.combinations(city_indices[1:], k-1)
    
    best_tour = None
    best_cost = float('inf')
    
    for subset in possible_tours:
        current_subset = [0] + list(subset) + [0]
        for tour_permutation in itertools.permutations(current_subset[1:-1]):
            full_tour = [0] + list(tour_permutation) + [0]
            current_cost = evaluate_tour(full_tour, cities)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = full_tour
                
    return best_tour, best_cost

# Coordinates of cities including depot
city_positions = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Find the best tour visiting exactly 8 cities including the depot
tour, total_cost = find_optimal_k_tsp_tour(city_positions, 8)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")