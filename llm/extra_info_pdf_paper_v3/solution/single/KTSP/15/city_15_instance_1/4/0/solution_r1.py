import math
from itertools import permutations

# Coordinates of the cities, where index corresponds to city ID
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour):
    """Given a tour of city indices, calculate the total distance of the tour."""
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_dist

def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    
    # Generate all combinations of 5 cities to visit besides the depot city
    for subset in permutations(range(1, len(cities)), 5):
        # Generate a tour by adding the depot city at the beginning and end
        tour = [0] + list(subset) + [0]
        
        # Calculate the cost for this tour
        cost = calculate_total_distance(tour)
        
        # Check if this tour has a lower cost than the found so far
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Find the shortest tour and its cost
tour, total_cost = find_shortest_tour()

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_cost)