from itertools import permutations
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for the depot and cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Generate all permutations of the cities (except the depot)
city_indices = list(cities.keys())
city_indices.remove(0)  # Remove the depot city, as it is the start and end point

def find_optimal_tour():
    optimal_tour = None
    optimal_cost = float('inf')
    optimal_max_dist = float('inf')
    
    # Test all permutations
    for perm in permutations(city_indices):
        tour = [0] + list(perm) + [0]  # Start and end at the depot city
        total_cost = 0
        max_distance = 0
        
        # Calculate total cost and max distance
        for i in range(len(tour) - 1):
            dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        # Check if this is the best tour found so far based on max distance criterion
        if max_distance < optimal_max_dist:
            optimal_max_dist = max_distance
            optimal_cost = total_static_cost = total_cost
            optimal_tour = tour
    
    return optimal_tour, optimal_cost, optimal_max_dist

optimal_tour, optimal_cost, optimal_max_dist = find_optimal_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))
print("Maximum distance between consecutive cities:", round(optimal_max_dist, 2))