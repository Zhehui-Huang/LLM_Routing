import math
import itertools

# Define the coordinates for each city, including the depot city
cities_coordinates = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    xa, ya = cities_coordinates[city_a]
    xb, yb = cities_coordinates[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Precompute distances between each pair of cities to speed up the search
distances = {(i, j): calculate_distance(i, j) for i in cities_coordinates for j in cities_coordinates}

# Function to find the shortest tour visiting exactly 4 cities including the depot
def find_shortest_tour():
    best_tour = None
    best_distance = float('inf')

    # We iterate over combinations of 3 cities (excluding the depot)
    for combo in itertools.combinations(range(1, 20), 3):
        # Generate all permutations of these 3 cities plus the depot
        for perm in itertools.permutations(combo):
            # Construct the tour starting and ending at the depot
            tour = [0] + list(perm) + [0]
            # Calculate the travel cost for this tour
            distance = sum(distances[(tour[i], tour[i+1])] for i in range(4))
            # Check if this tour is better than what we have found before
            if distance < best_distance:
                best_distance = distance
                best_tour = tour

    return best_tour, best_distance

# Execute the function to obtain the optimal tour and its cost
optimal_tour, optimal_distance = find_shortest_tour()

# Output the result
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_distance)