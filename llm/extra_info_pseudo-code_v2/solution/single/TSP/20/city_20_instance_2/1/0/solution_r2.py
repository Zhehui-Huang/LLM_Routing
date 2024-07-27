import math
from itertools import permutations

# Coordinates of the cities including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Brute force approach to find the optimal tour (temporary simple solution)
def find_min_tour():
    N = len(cities)
    min_tour = None
    min_cost = float('inf')
    
    # Generate all possible tours starting and ending at the depot (skipping index 0 in permutations)     
    for tour in permutations(range(1, N)):
        current_cost = distance(cities[0], cities[tour[0]])  # Start at the depot
        for i in range(1, len(tour)):
            current_cost += distance(cities[tour[i - 1]], cities[tour[i]])
        current_cost += distance(cities[tour[-1]], cities[0])  # Return to the depot
        
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = tour
    
    return [0] + list(min_tour) + [0], min_cost

# Finding the shortest tour using the proposed method
tour, total_cost = find_min_tour()

# Print the tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)