import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour, cities):
    return sum(calculate_distance(cities[tour[i - 1]], cities[tour[i]]) for i in range(len(tour)))

def initial_tour(num_cities):
    return list(range(num_cities)) + [0]

def lin_kernighan_tour(initial_tour, cities):
    # This is a placeholder for a full Lin-Kernighan implementation.
    # Here we use a simple strategy by checking all permutations since problem size is small.
    num_cities = len(cities)
    best_tour = initial_tour
    best_distance = calculate_total_distance(best_tour, cities)
    
    # Check all city permutations for the best one (only feasible for very small problems)
    for perm in permutations(range(1, num_cities)):
        current_tour = [0] + list(perm) + [0]
        current_distance = calculate_total_distance(current_tour, cities)
        if current_distance < best_distance:
            best_tour, best_distance = current_tour, current_distance
    
    return best_tour, best_distance

cities = [
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

# Entry point for finding the best TSP tour
initial_solution = initial_tour(len(cities))
tour, total_cost = lin_kernighan_tour(initial_solution, cities)

output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}"
print(output)