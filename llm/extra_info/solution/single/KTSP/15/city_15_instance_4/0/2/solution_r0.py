import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # Close the loop to the start city
    return cost

def find_shortest_tour(cities, n_cities_to_visit):
    all_city_indices = list(range(1, len(cities)))
    
    # Generate all combinations of cities to visit (excluding the depot, which is city 0)
    from itertools import combinations
    possible_combinations = combinations(all_city_indices, n_cities_to_visit - 1)  # -1 because we include the depot
    
    best_tour = None
    best_cost = float('inf')
    
    for combination in possible_combinations:
        # Always start with the depot city, included in the tour
        current_combination = [0] + list(combination)
        
        # Generate all permutations of the selected cities to find minimal route
        for permutation in permutations(current_combination[1:]):  # without the depot
            current_tour = [0] + list(permutation) + [0]  # start and end at the depot
            current_cost = total_tour_cost(current_tour, cities)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour
                
    return best_tour, best_cost

# Define locations of cities as (x, y) coordinates
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

# The robot needs to start and end at city 0 and visit exactly 12 cities
n_cities_to_visit = 12

# Get the shortest path and its cost using the defined function
optimal_tour, minimal_cost = find_shortest_tour(cities, n_cities_to_visit)

print("Tour:", optimal_tour)
print("Total travel cost:", minimal_cost)