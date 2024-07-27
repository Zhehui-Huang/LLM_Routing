import itertools
import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour, city_coords):
    """Calculate total travel cost of the given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return cost

def find_shortest_tour(cities, depot_index, k):
    """Find the shortest tour that includes exactly k cities starting and ending at the depot city."""
    all_combinations = itertools.combinations([i for i in range(len(cities)) if i != depot_index], k-1)
    city_coords = [tuple(cities[i]) for i in range(len(cities))]
    shortest_tour = None
    shortest_tour_cost = float('inf')
    
    for comb in all_combinations:
        # Adding depot city at start and end of the tour
        current_combination = [depot_index] + list(comb) + [depot_index]
        all_permutations = itertools.permutations(current_combination[1:-1])  # Permute internal cities only
        
        for perm in all_permutations:
            current_tour = [depot_index] + list(perm) + [depot_index]
            current_cost = calculate_tour_cost(current_tour, city_coords)
            if current_cost < shortest_tour_cost:
                shortest_tour = current_tour
                shortest_tour_settings_cost = current_cost
    
    return shortest_tour, shortest_tour_cost

# Coordinates for each city including the depot
cities_coordinates = [
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

# Parameters
depot_index = 0
k_visits = 8

# Find the shortest tour
shortest_tour, total_cost = find_shortest_tour(cities_coordinates, depot_index, k_visits)
print("Tour:", shortest_tour)
print("Total travel cost:", round(total_cost, 2))