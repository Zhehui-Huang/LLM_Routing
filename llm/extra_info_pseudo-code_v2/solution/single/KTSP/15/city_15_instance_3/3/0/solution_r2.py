import itertools
import math

# City coordinates (index corresponds to city number, index 0 is depot)
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64),
    (32, 79)
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    """Calculate the total distance of a tour."""
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]]) # round trip
    return total_distance

# Generate all possible tours that visit exactly 10 cities including the depot
# and return to the depot
def find_optimal_tour():
    best_distance = float('inf')
    best_tour = None
    for city_combination in itertools.combinations(range(1, 15), 9): # Combinations of 9 other cities
        tour = [0] + list(city_combination) + [0]
        distance = calculate_total_distance(tour)
        if distance < best_distance:
            best_distance = distance
            best_tour = tour
    return best_tour, best_distance

# Solve the problem
optimal_tour, optimal_distance = find_optimal_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_distance, 2))