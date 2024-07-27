from itertools import combinations, permutations
import math

# Define the coordinates of the cities
cities = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all tour combinations starting and ending at the depot
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    # Choose 3 other cities plus depot (index '0')
    city_combinations = combinations(range(1, 15), 3)
    
    for cities_subset in city_combinations:
        full_tour = [0] + list(cities_subset) + [0]
        
        # Generate permutations of the middle cities
        for perm in permutations(cities_subset):
            # Create the complete tour including the depot city
            current_tour = [0] + list(perm) + [0]
            # Calculate the travel cost
            total_travel_cost = sum(euclidean_distance(cities[current_tour[i]], cities[current_tour[i + 1]]) for i in range(len(current_tour) - 1))
            
            # Check if this is the shortest tour found so far
            if total_travel_cost < min_distance:
                min_distance = total_travel_cost
                best_tour = current_tour
                
    return best_tour, min_distance

# Solve the problem
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)