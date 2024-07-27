import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

cities = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]
num_cities = len(cities)

# Calculate distances between each city
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

def find_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    # Generate all permutations of city indices from 1 to num_cities - 1 (excluding the depot city 0)
    for perm in permutations(range(1, num_cities)):
        # Add the depot city at the start and end of the tour
        tour = [0] + list(perm) + [0]
        
        # Calculate the total cost and maximum distance between consecutive cities in this tour
        total_cost = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            dist = distances[tour[i]][tour[i+1]]
            total_cost += dist
            if dist > max_distance:
                max_distance = dist

        # Update the best tour found based on min_max_distance
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            total_min_cost = total_cost

    return best_tour, total_min_cost, min_max_distance

best_tour, total_cost, max_dist = find_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")