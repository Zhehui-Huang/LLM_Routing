import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp(coords):
    num_cities = len(coords)
    
    # Generate all possible tours
    all_tours = permutations(range(1, num_cities))
    
    best_tour = None
    min_max_distance = float('inf')
    total_cost_best_tour = float('inf')
    
    for tour in all_tours:
        tour = (0,) + tour + (0,)
        max_distance = 0
        total_cost = 0
        
        for i in range(len(tour) - 1):
            distance = calculate_distance(coords[tour[i]], coords[tour[i + 1]])
            total_cost += distance
            if distance > max_distance:
                max_distance = distance
        
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_cost_best_tour):
            best_tour = tour
            min_max_distance = max_distance
            total_cost_best_tour = total_cost
    
    return list(best_tour), total_cost_best_tour, min_max_distance

coords = [
    (84, 67),  # City 0 - Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

tour, total_cost, max_distance_between_cities = solve_tsp(coords)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")