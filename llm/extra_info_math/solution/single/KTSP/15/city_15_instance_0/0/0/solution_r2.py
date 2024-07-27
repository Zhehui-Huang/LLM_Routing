import itertools
import math

# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to find the shortest tour visiting exactly `k` cities including the depot
def find_shortest_tour(cities, k):
    num_cities = len(cities)
    min_distance = float('inf')
    best_path = None
    
    # Iterate through combinations that choose k-1 cities excluding the depot (index 0)
    for cities_indices in itertools.combinations(range(1, num_cities), k-1):
        cities_indices = (0,) + cities_indices  # Always include the depot as start and end
        # Generate permutations of the selected cities and calculate tour distance
        for perm in itertools.permutations(cities_indices):
            # Close the loop - return to the depot
            perm = perm + (perm[0],)
            current_distance = sum(calculate_distance(cities[perm[i]], cities[perm[i+1]]) for i in range(len(perm)-1))
            # Update best path if current is shorter
            if current_distance < min_distance:
                min_distance = current_distance
                best_path = perm

    return best_path, min_distance

# City coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Define how many cities (including the depot) we want to visit
k = 4

# Solve the problem
tour, total_cost = find_shortest_tour(cities, k)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))