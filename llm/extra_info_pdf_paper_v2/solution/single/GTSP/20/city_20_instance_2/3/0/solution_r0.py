import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to find an initial solution by selecting the nearest city from each group to the depot
def select_initial_cities():
    initial_cities = []
    depot = cities[0]
    
    for group in groups:
        nearest_city = min(group, key=lambda city: calculate_distance(depot, cities[city]))
        initial_cities.append(nearest_city)
    
    return initial_cities

# Calculate the total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_objective_distance(tour[i], tour[i + 1])
    return total_cost

# A basic Local Search to attempt improvements on the initial solution
def local_search(initial_tour):
    best_tour = initial_tour
    best_cost = tour_cost(initial_tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour)):
                if j - i == 1: continue # Skip if cities are consecutive -- no change possible
                new_tour = best_tour[:]
                new_tour[i:j] = reversed(best_tour[i:j]) # Reverse segment of tour
                new_cost = tour_cost(new_tou)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
                
    return best_tour, best_cost

initial_cities = select_initial_cities()
initial_tour = [0] + initial_cities + [0]
optimized_tour, optimized_cost = local_search(initial_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)