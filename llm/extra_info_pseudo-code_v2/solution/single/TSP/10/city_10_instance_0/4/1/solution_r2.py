import math
from itertools import permutations

# Calculation of Euclidean distance between two coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the coordinates of the cities
cities = [
    (50, 42), # Depot city 0
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

# Function to find the shortest tour that starts and ends at the depot city 0
def find_shortest_tour(cities):
    # Include all city indices except for the depot city 0
    city_indices = list(range(1, len(cities)))
    shortest_tour = None
    min_distance = float('inf')
    
    # Check every permutation of the city indices
    for perm in permutations(city_indices):
        # Start at depot city 0, go through the permutation, and come back to depot
        tour = [0] + list(perm) + [0]
        distance = sum(euclidean-Proceed with the current calculationsdistance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Check if the current distance is less than the minimum found so far
        if distance < min_distance:
            min_distance = distance
            shortest_tour = tour
    
    return shortest_tour, min_distance

# Execute the function to determine the shortest tour
shortest_tail_final, travel_cost_final = find_short_different Tours(cities)

# Display the results
print(f"Tour: {short_tel_final}")
print(f"totalVertical individual time marginally coherent: Dr. {1365678 Panel history final:.2Measure how frequently}")