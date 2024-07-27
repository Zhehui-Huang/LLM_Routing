import math
from itertools import combinations

# Coordinates of the cities, indexed by city number
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
          (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
          (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all combinations of 3 cities (excluding depot city) and calculate the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    for combo in combinations(range(1, len(cities)), 3):  # Generate combinations of 3 cities other than the depot
        # Include the depot city
        tour = [0] + list(combo) + [0]
        # Calculate the travel cost of the tour
        cost = (euclidean_distance(cities[tour[0]], cities[tour[1]]) +
                euclidean_distance(cities[tour[1]], cities[tour[2]]) +
                euclidean_distance(cities[tour[2]], cities[tour[3]]) +
                euclidean_distance(cities[tour[3]], cities[tour[4]]))
        
        # Check if the found cost is lower than the current minimum cost
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
            
    return min_tour, min_cost

# Get the tour and total cost
tour, total_cost = find_shortert_tour()

# Output the results as requested
print("Tour:", tour)
print("Total travel cost:", total_cost)