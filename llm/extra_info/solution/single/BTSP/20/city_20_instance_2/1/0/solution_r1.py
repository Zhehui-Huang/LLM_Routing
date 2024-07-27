from math import sqrt
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[cityemainin2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Gather city indices except the depot
city_indices = list(cities.keys())[1:]

# Initialize variables to find the optimal tour
optimal_tour = None
min_max_distance = float('inf')
total_min_cost = float('inf')

# Loop through all permutations, limiting to a manageable sample size for illustration
for perm in permutations(city_indices, 6):  # Limiting to permutations of 6 for demonstration; increase for exhaustive search
    tour = (0,) + perm + (0,)
    
    # Calculate max distance and total cost for this tour permutation
    max_distance = 0
    total_cost = 0
    for i in range(len(tour)-1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Update the optimal tour if the new permutation is better
    if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_min_cost):
        optimal_tour = tour
        min_max_distance = max_distance
        total_min_cost = total_cost

# Display results
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {total_min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")