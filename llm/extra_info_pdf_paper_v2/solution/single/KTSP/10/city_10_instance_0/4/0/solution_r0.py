import itertools
import math

# City coordinates index is corresponding to their given number
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

def euclidean_distance(city_a, city_b):
    # Calculate Euclidean distance between city_a and city_b
    return math.sqrt((coordinates[city_b][0] - coordinates[city_a][0])**2 + (coordinates[city_b][1] - coordinates[city_a][1])**2)

def calculate_tour_cost(tour):
    # Sum the cost of traversing between consecutive cities in the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_t = euclidean_distance(tour[i], tour[i + 1])
        total_cost += int(total_t)
        # Include float to int conversion to match the distance example output as an integer
    return total_cost

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Generate combinations of 3 cities excluding depot city (index 0)
    city_indices = list(range(1, 10))
    for cities in itertools.combinations(city_indices, 3):
        # Always include depot city in the tour
        current_permutations = list(itertools.permutations(cities))
        for perm in current_permutations:
            tour = [0] + list(perm) + [0]
            cost = calculate_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
                
    return best_tour, best_cost

# Solve the problem
best_tour, best_cost = find_best_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")