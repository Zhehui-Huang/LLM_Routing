import math
from itertools import permutations

# Define cities coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 88), (97, 28), 
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Function to calculate Euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = dist(cities[i], cities[j])

# Finding the optimal tour minimizing the maximum edge length
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Since the problem is small, using permutations to find the best route
for perm in permutations(range(1, n)):
    # Adding depot city 0 at start and end
    tour = [0] + list(perm) + [0]
    
    # Calculate total cost and max distance of this tour
    total_cost = 0
    max_leg_distance = 0
    for k in range(len(tour) - 1):
        leg_distance = distance_matrix[tour[k]][tour[k+1]]
        total_cost += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_distance = leg_distance
    
    # Check if this tour is better
    if max_leg_distance < best_max_distance or (max_leg_index == best_max_distance and total_cost < best_total_cost):
        best_tour = tour
        best_max_distance = max_leg_distance
        best_total_cost = total_cost

# Output the results in the requested format
print("Tour:", best_tour)
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")