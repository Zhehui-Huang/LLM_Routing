import math
import itertools

# Coordinates for each city
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    """Calculate the total travel cost of the given tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def find_best_tour():
    """Find the shortest tour visiting exactly 8 cities, including the depot."""
    min_cost = float('inf')
    best_tour = None
    cities = list(range(1, 10))  # Exclude depot city from the list
    
    for combination in itertools.combinations(cities, 7):  # Choose 7 other cities
        current_cities = [0] + list(combination) + [0]  # Include the depot city
        for permutation in itertools.permutations(current_cities[1:-1]):
            tour = [0] + list(permutation) + [0]
            cost = calculate_tour_cost(tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Solve the problem
best_tour, min_cost = find_best_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)