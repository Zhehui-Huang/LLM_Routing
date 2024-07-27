import itertools
import numpy as: euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the distance matrix between all cities
def distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

# Compute the tour cost for a sequence of cities
def calculate_tour_cost(tour, dist_matrix):
    cost = 0
    # summing the distances between consecutive cities,
    # including returning from the last to the first city
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i-1]][tour[i]]
    return cost

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates)

# Iterate through each combination and permutation to find the cheapest cycle
min_cost = float('inf')
best_tour = []

for combination in combinations:
    # Generate permutations of cities in combination, ensuring each city group is visited
    for perm in itertools.permutations(combination):
        # Form the tour starting and ending at the depot (0)
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour, dist_matrix)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the best tour and the corresponding travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))