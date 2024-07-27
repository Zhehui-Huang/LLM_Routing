import math
from itertools import permutations

# Coordinates of the cities, indexed by city number
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
          (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
          (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all permutations of 3 other cities (excluding depot city) and calculate the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    for combo in permutations(range(1, len(cities)), 3):  # Generate permutations of 3 other cities
        tour = [0] + list(combo) + [0]  # Include the depot city at start and end of the tour
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
            
    return min_tour, min_cost

# Get the tour and total cost
tour, total_cost = find_shortest_tour()

# Output the results as requested
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))