import math
from itertools import permutations, combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # Closing the loop back to depot
    return cost

def find_shortest_tour(cities, n_cities_to_visit):
    all_city_indices = list(range(1, len(cities)))
    best_cost = float('inf')
    best_tour = None
    
    for combination in combinations(all_city_indices, n_cities_to_visit - 1):  # include depot in final tour count
        current_combination = [0] + list(combination)  # start from the depot
        
        # Generate all permutations of the selected cities to find the minimal route
        for permutation in permutations(current_combination[1:]):  # start permutations from first city other than depot
            current_tour = [0] + list(permutation) + [0]  # add depot to beginning and end
            current_cost = total_tour_cost(current_tour, cities)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour

    return best_tour, best_cost

# Define locations (x, y) for each city including the depot
cities = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Number of cities to visit including the depot
n_cities_to_visit = 12

# Find shortest tour
optimal_tour, minimal_cost = find_shortest_tour(cities, n_cities_to_visit)

print("Tour:", optimal_tour)
print("Total travel cost:", minimal_cost)