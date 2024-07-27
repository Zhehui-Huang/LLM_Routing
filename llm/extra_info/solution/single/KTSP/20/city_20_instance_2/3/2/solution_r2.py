import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def get_shortest_tour(cities):
    n = len(cities)
    all_combinations = itertools.combinations(range(1, n), 9)  # All combinations of 9 cities (excluding depot)
    
    shortest_tour = None
    min_cost = float('inf')
    
    for subset in all_combinations:
        all_permutations = itertools.permutations(subset)
        for tour in all_permutations:
            current_tour = [0] + list(tour) + [0]
            current_cost = sum(calculate_distance(cities[current_tour[i]], cities[current_tour[i+1]]) for i in range(len(current_tour) - 1))
            
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_tour = current_tour
    
    return shortest_tour, min_cost

# Coordinates of the cities (depot + 19 other cities)
cities = [
    (3, 26),   # Depot
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

shortest_tour, min_cost = get_shortest_tour(cities)
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)