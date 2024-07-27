import itertools
from math import sqrt, inf

# Coordinates of cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute distance matrix
def compute_distances(coords):
    n = len(coords)
    dists = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dists[i][j] = euclidean_distance(coords[i], coords[j])
            else:
                dists[i][j] = inf
    return dists

distances = compute_distances(coordinates)

# Find minimum tour starting and ending at the depot city (0)
def find_min_tour(start_city, num_cities):
    cities = list(range(1, len(coordinates)))  # cities excluding the depot
    shortest_tour = None
    min_cost = inf
    
    for subset in itertools.combinations(cities, num_cities-1):  # Choose 15 additional cities, including the depot
        current_cities = [start_city] + list(subset)
        for tour in itertools.permutations(current_cities):
            tour_cost = 0
            tour = list(tour) + [start_city]  # Close the loop, back to the depot
            for i in range(len(tour) - 1):
                tour_cost += distances[tour[i]][tour[i + 1]]
            
            if tour_cost < min_cost:
                min_cost = tour_cost
                shortest_tour = tour
    
    return shortest_tour, min_cost

# Execute the function with appropriate parameters
tour, total_cost = find_min_tour(0, 16)

# Output the results
print("Tour:", tour)
print("Total travel is: {:.2f}".format(total_cost))