import itertools
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_shortest_tour(cities):
    depot = cities[0]
    other_cities = cities[1:]
    min_cost = float('inf')
    best_tour = None
    
    for comb in itertools.combinations(other_cities, 3):
        for perm in itertools.permutations(comb):
            tour = [depot] + list(perm) + [depot]
            total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = tour
                
    return best_tour, min_cost

# Coordinates of each city including the depot (index 0)
cities = [
    (8, 11),   # City 0 - Depot
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

best_tour, total_cost = find_shortest_tour(cities)
best_tour_indices = [cities.index(city) for city in best_tour]

print("Tour:", best_tour_indices)
print("Total travel cost:", round(total_cost, 2))