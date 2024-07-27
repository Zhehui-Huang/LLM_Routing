import math
import itertools

# Coordinates of the cities indexed from 0 (depot) to 9
coords = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_distances(coords):
    """Calculate a matrix of distances between each pair of coordinates."""
    num_cities = len(coords)
    return [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

def find_min_tour(distances):
    """This function uses a simple heuristic to create a tour that starts and ends at the depot."""
    num_cities = len(distances)
    unvisited = set(range(1, num_cities))
    tour = [0]
    last = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[last][x])
        tour.append(next_city)
        last = next_city
        unvisited.remove(next_city)

    tour.append(0)  # return to the depot
    return tour

def evaluate_tour(tour, distances):
    """Calculate the total distance and the maximum leg distance for a tour."""
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_leg_distance

# Calculate distances between all pairs of cities
distances = calculate_distances(coords)

# Find a tentative tour using a simple heuristic
tour = find_min_tour(distances)

# Evaluate the tour for total and maximum leg distances
total_cost, max_leg_distance = evaluate_tour(tour, distances)

# Output format
output_tour = f"Tour: {tour}"
output_cost = f"Total travel cost: {total_cost:.2f}"
output_max_dist = f"Maximum distance between consecutive cities: {max_leg_distance:.2f}"

print(output_tour)
print(output_cost)
print(output_max_dist)