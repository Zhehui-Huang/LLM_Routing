import math
from itertools import permutations

# Define city coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6),  # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),  # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Function to calculate Euclidean distance
def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

# Generate distances matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Find the optimal tour minimizing the maximum distance between consecutive cities
def find_bottleneck_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')

    # Permutate over cities excluding the depot (index 0)
    for perm in permutations(range(1, len(cities))):
        # Create a full tour by appending the depot at start and end
        tour = [0] + list(perm) + [0]
        # Compute distances between consecutive cities in the tour
        tour_distances = [distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1)]
        max_tour_distance = max(tour_distances)
        total_tour_cost = sum(tour_distances)
        
        # Update the best tour if a new optimal tour is found
        if max_tour_distance < min_max_distance or (max_tour_distance == min_max_distance and total_tour_cost < total_min_cost):
            best_tour = tour
            min_max_distance = max_tour_distance
            total_min_cost = total_tour_cost

    return best_tour, total_min_cost, min_max_distance

# Execute the function to get the results
tour, total_cost, max_distance = find_bottleneck_tour()

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")