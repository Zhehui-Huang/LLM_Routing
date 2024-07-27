import math
from itertools import permutations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a matrix of distances between each pair of cities
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Approximate a solution using a simple permutation-based method
# (Note: This is a computationally expensive step and not efficient for large number of cities)
def find_shortest_tour():
    shortest_tour = None
    min_cost = float('inf')

    for permutation in permutations(range(1, num_cities)):
        # Include the depot as start and end point
        tour = [0] + list(permutation) + [0]
        # Calculate the total cost of this tour
        total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        # Update the shortest tour found
        if total_cost < min_cost:
            min_cost = total_cost
            shortest_tour = tour

    return shortest_tour, min_cost

# Find and print the shortest tour and the total travel cost
shortest_tour, total_cost = find_shortest_tour()
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost:.2f}")