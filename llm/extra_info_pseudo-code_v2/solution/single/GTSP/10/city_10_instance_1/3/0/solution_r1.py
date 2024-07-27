import math
from itertools import product

# Coordinates of the cities
city_locations = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    x1, y1 = city_locations[city1]
    x2, y0 = city_locations[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y0) ** 2)

def total_tour_cost(tour):
    # Computes the total cost of the provided tour
    total_cost = calculate_distance(0, tour[0])  # from depot to first city
    for i in range(1, len(tour)):
        total_cost += calculate_distance(tour[i-1], tour[i])
    total_cost += calculate_distance(tour[-1], 0)  # from last city back to depot
    return total_cost

def find_shortest_tour():
    all_group_combinations = list(product(*[groups[key] for key in sorted(groups.keys())]))
    best_path = None
    min_cost = float('inf')
    
    for combination in all_group_combinations:
        tour = list(combination)
        cost = total_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_path = tour
    
    return [0] + best_path + [0], min_cost  # Adding depot as start and end in the path

# Find the optimal solution
optimal_tour, optimal_cost = find_shortest_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")