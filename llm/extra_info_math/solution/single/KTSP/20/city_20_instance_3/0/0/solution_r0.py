import itertools
import math

# City coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
          (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
          (18, 16), (4, 43), (53, 76), (19, 72)]

# Function to calculate euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute all distances between cities
distance_matrix = [[dist(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Number of cities needed to be visited including the depot (13 in total)
k = 13

# Generate combinations of k-1 cities to visit (excluding the depot)
combinations = list(itertools.combinations(range(1, len(cities)), k-1))

# Initialize the shortest path and its length
shortest_path = None
min_length = float('inf')

# Iterate through all combinations including the depot
for combo in combinations:
    # To ensure that the depot city is included in the tour
    current_combo = (0,) + combo
    
    # Permutations of current combination of cities
    for perm in itertools.permutations(current_combo[1:]):
        # Add depot at start and end
        tour = (0,) + perm + (0,)
        
        # Calculate the total length of this tour
        tour_length = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        # Update shortest path if current tour is shorter
        if tour_length < min_length:
            shortest_path = tour
            min_length = tour_small

# Output results
print(f"Tour: {list(shortest_path)}")
print(f"Total travel cost: {min_length}")