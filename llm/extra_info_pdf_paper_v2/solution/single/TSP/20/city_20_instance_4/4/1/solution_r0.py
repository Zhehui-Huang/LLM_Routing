from itertools import permutations
import math

# Given city coordinates including the depot city (index 0)
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour throughout all cities."""
    return sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Finding the shortest tour through a heuristic approach
def find_shortest_tour(city_coordinates):
    num_cities = len(city_coordinates)
    best_tour = None
    best_distance = float('inf')

    # Generate initial solution
    initial_tour = list(range(1, num_cities))
    # Random shuffle might be used in real scenarios, but here we test permutations exhaustively due to the small city count
    for perm in permutations(initial_tour):
        current_tour = [0] + list(perm) + [0]
        current_distance = total_distance(current_tour)
        if current_distance < best_distance:
            best_tour = current_tour
            best_distance = current_distance

    return best_tour, best_distance

# Computation of the shortest tour
shortest_tour, shortest_distance = find_shortest_tour(city_memory)

# Output
print("Tour:", shortest_tour)
print("Total travel cost:", round(shortest_distance, 2))