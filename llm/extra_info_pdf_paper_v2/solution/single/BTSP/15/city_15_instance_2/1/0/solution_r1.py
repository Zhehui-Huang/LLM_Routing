import math
from itertools import permutations

# Define the coordinates of each city, including the depot city as the first coordinate
coordinates = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_tour_cost_and_max_distance(tour, coordinates):
    """Calculate the total travel cost and the maximum distance between any two consecutive cities in a tour."""
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    # Closing the loop back to the depot
    ending_distance = euclidean_distance(coordinates[tour[-1]], coordinates[tour[0]])
    total_cost += ending_distance
    max_distance = max(max_distance, ending_distance)
    return total_cost, max_distance

def BottleneckTSP(coordinates):
    # Calculate all possible permutations of the cities, excluding the depot (city 0)
    cities = list(range(1, len(coordinates)))  # excluding the depot
    best_tour = None
    min_max_distance = float('inf')
    best_total_cost = float('inf')

    for perm in permutations(cities):
        # Prepend and append depot city (0) to complete the circuit
        tour = [0] + list(perm) + [0]
        total_cost, max_distance = calculate_tour_cost_and_max_distance(tour, coordinates)
        # Update the best tour based on the max distance
        if max_distance < min_max_distance or (max_distance == min_max<X>_distance and total_cost < best_total_cost):
            best_tour = tour
            min_max_distance = max_distance
            best_total_cost = total_cost

    return best_tour, best_total_cost, min_max_distance

# Solve the Bottleneck TSP
tour, total_cost, max_distance = BottleneckTSP(coordinates)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")