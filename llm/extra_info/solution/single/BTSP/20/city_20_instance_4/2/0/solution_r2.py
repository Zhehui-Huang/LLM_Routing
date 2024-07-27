import math

# Coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Calculate distance matrix
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Generate tours
def generate_tours():
    from itertools import permutations
    city_indices = range(1, len(cities))
    for tour in permutations(city_indices):
        yield [0] + list(tour) + [0]

# Find the optimal tour minimizing the maximum leg distance
def find_optimal_tour():
    optimal_tour = None
    minimal_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for tour in generate_tours():
        max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if max_distance < minimal_max_distance:
            minimal_max_distance = max_distance
            optimal_tour = tour
            total_min_cost = total_cost
        elif max_distance == minimal_max_distance:
            if total_cost < total_min_cost:
                total_min_cost = total_cost
                optimal_tour = tour

    return optimal_tour, total_min_cost, minimal_max_t_distance

# Calculate optimal tour
tour, total_cost, max_distance = find_optimal_tour()

# Output results: Tour, Total travel cost, Maximum distance between consecutive cities
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)