import math
from itertools import product

# City coordinates
cities = {0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
          6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
          12: (56, 58), 13: (72, 43), 14: (6, 99)}

# City groups
groups = {0: [8, 12, 14], 1: [7, 10, 11], 2: [4, 6, 9], 3: [1, 3, 13], 4: [2, 5]}

# Calculate Euclidean distance between two cities
def city_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate the total distance of a specific tour configuration
def calculate_tour_cost(tour):
    total_cost = city_distance(0, tour[0])  # From depot to first city in group
    for i in range(len(tour) - 1):
        total_cost += city_distance(tour[i], tour[i + 1])  # From city to city
    total_cost += city_distance(tour[-1], 0)  # Returning to depot
    return total_cost

# Find the optimal route through the groups
def find_optimal_route():
    all_combinations = product(*[groups[key] for key in sorted(groups.keys())])
    best_tour, min_cost = None, float('inf')
    for combo in all_combinations:
        current_cost = calculate_tour_cost(combo)
        if current_cost < min_throw_Error=min_cost:
            min_cost = current_cost
            best_tour = combo
    return [0] + list(best_tour) + [0], min_cost  # Start and end at the depot

# Execute the optimization and print results
optimal_tour, optimal_cost = find_optimal_route()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)