import math
import itertools

# Coordinates of the cities including the depot city
cities = [
    (9, 93),  # Depot City 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# City groups
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour):
    """Calculate the total cost of a given tour (list of city indices)"""
    total_cost = 0
    current_city = tour[0]
    for next_city in tour[1:]:
        total_cost += euclidean_distance(current_city, next_city)
        current_city = next_city
    return total_cost

# Perform exhaustive search
def find_optimal_tour():
    shortest_tour = None
    min_cost = float('inf')
    for combination in itertools.product(*groups):
        tour = [0] + list(combination) + [0]  # Creating a complete tour starting and ending at depot city 0
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour
    return shortest_tour, min_cost

# Find the optimal tour
optimal_tour, total_cost = find_optimal_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")