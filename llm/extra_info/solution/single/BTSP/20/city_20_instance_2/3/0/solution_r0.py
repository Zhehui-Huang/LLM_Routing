import math
from itertools import permutations

# Define the coordinates of each city, including the depot
cities = [
    (3, 26),  # Depot
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairwise city distances
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Finding a tour that minimizes the max distance between any two consecutive cities
def find_min_max_tour():
    best_tour = None
    best_max_dist = float('inf')
    best_total_cost = float('inf')

    # Generate all permutations of city indices except the depot
    for tour in permutations(range(1, num_cities)):
        # Include the depot at the start and end of the tour
        current_tour = [0] + list(tour) + [0]
        
        # Compute the total travel cost and maximum distance of this tour
        total_cost = 0
        max_dist = 0
        for i in range(len(current_tour) - 1):
            dist = distances[current_tour[i]][current_tour[i + 1]]
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        
        # If this tour is better, update the best tour found so far
        if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < best_total_cost):
            best_tour = current_tour
            best_max_dist = max_dist
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_dist

# Execute the function to find the optimal tour
tour, total_cost, max_dist = find_min_max_tour()

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)