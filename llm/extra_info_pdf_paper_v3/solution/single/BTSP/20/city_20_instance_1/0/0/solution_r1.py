import itertools
import math

# Define cities coordinates with a subset of cities for feasibility in permutations
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Exhaustive search to find the optimal tour
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = []
    all_cities = list(cities.keys())[1:]  # Exclude the depot when generating permutations
    
    for perm in itertools.permutations(all_cities):
        tour = [0] + list(perm) + [0]  # start and end at the depot city
        max_distance = 0
        total_distance = 0
        
        for i in range(len(tour) - 1):
            dist = calculate_distance(tour[i], tour[i + 1])
            total_distance += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour
            optimal_total_distance = total_distance
    
    return optimal_tour, optimal_total_distance, min_max_distance

# Execute the function and capture the output
optimal_tour, total_distance, max_distance = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)