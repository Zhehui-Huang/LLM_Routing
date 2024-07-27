import itertools
import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, coordinates):
    """ Calculates the cost of the given tour based on the coordinates. """
    cost = 0
    for i in range(1, len(tour)):
        cost += calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def find_shortest_tour(cities):
    """ Find the shortest possible tour that includes the depot city and ends back at the depot. """
    # Compute full permutation excluding the depot city (index 0), but include depot in the tour calculation.
    min_cost = float('inf')
    optimal_tour = []
    
    # Generate all combinations of 11 other cities from cities 1-14 to create a total tour of 12 cities
    for city_combo in itertools.combinations(range(1, 15), 11):
        current_tour = [0] + list(city_combo) + [0]
        permutations = itertools.permutations(current_tour[1:-1])
        
        for perm in permutations:
            perm_tour = [0] + list(perm) + [0]
            cost = total_tour_bhbj_cost(perm_tour, cities)
            if cost < min_cost:
                min_cost = cost
                optimal_tour = perm_tour
                
    return optimal_tour, min_cost

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Find optimal tour and cost for the TSP
optimal_tour, total_cost = find_shortest_tour(cities)

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")