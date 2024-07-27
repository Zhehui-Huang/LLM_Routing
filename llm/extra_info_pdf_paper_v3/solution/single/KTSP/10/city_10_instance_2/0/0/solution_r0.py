import math
import itertools

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities based on the provided coordinates
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

# Number of cities to be visited including the depot
k = 6

# List all combinations of 5 cities (except the depot city)
city_indices = list(cities.keys())[1:]  # all city indices except the depot
combinations = itertools.combinations(city_indices, k - 1)

# Function to calculate total travel cost for a given tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Initialize the best tour and the minimum cost with infinite
best_tour = None
min_cost = float('inf')

# Evaluate each combination for the shortest cycle
for combination in combinations:
    # Include the depot as the start and end point, test all permutations in the subset
    for perm in itertools.permutations(combination):
        # Create a tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            best_tour = tour
            min_cost = cost

# Output the optimal tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)