import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define cities coordinates
cities = [
    (50, 42),  # Depot city 0
    (41, 1), 
    (18, 46), 
    (40, 98), 
    (51, 69), 
    (47, 39), 
    (62, 26), 
    (79, 31), 
    (61, 90), 
    (42, 49)
]

# Find the shortest tour through all cities starting and ending at the depot
def find_shortest_tour(cities):
    # Include all city indices except for the depot city 0
    city_indices = list(range(1, len(cities)))
    shortest_tour = None
    min_distance = float('inf')
    
    # Check every permutation of the city indices
    for perm in permutations(city_indices):
        # Start at depot city 0, go through the permutation, and come back to depot
        tour = [0] + list(perm) + [0]
        distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        if distance < min_distan ...
        ce:
            min_distance = distance
            shortest_tour = tour
            
    return shortest_tour, min_distance

# Get the shortest tour and travel cost
shortest_tour, travel_cost = find_shortest_tour(cities)

# Print the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {travel_cost:.2f}")