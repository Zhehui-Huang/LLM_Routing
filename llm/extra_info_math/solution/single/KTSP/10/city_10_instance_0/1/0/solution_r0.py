from itertools import combinations
import math

# Define the cities and their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to compute the total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Define the number of cities to visit including the depot city
k = 4

# Generate all combinations of 3 cities (excluding the depot city) to pair with the depot city
city_combinations = combinations([i for i in cities if i != 0], k - 1)

# Initialize the optimal tour and its cost
optimal_tour = None
optimal_cost = float('inf')

# Explore all combinations to find the optimal tour
for combination in city_combinations:
    # Create the candidates for the tours by including the depot city
    current_tour = [0] + list(combination) + [0]
    
    # Generate all permutations of the selected cities
    for perm in itertools.permutations(combination):
        # Create the tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        cost = total_distance(tour)
        
        # Update the optimal tour and cost if this tour is better
        if cost < optimal_cost:
            optimal_tour = tour
            optimal_cost = cost

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)