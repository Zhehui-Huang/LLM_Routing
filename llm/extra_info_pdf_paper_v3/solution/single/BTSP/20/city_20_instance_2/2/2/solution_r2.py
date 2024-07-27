import math

# City coordinates indexed from city 0 (Depot) to city 19.
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def compute_distance(coord1, coord2):
    """Compute Euclidean distance between two cities given their coordinates."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def nearest_neighbor_tour(start_index):
    num_cities = len(city_coordinates)
    unvisited = set(range(num_cities))
    unvisited.remove(start_index)
    tour = [start_index]
    current_index = start_index
    
    while unvisited:
        next_index = min(unvisited, key=lambda idx: compute_distance(city_coordinates[current_index], city_coordinates[idx]))
        tour.append(next_index)
        unvisited.remove(next_index)
        current_index = next_index
    
    tour.append(start_index)  # Return to depot
    return tour

def tour_cost_and_max_distance(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = compute_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Using the nearest neighbor heuristic to calculate a quick solution
tour = nearest_neighbor_tour(0)
total_cost, max_distance = tour_cost_and_max_distance(tour)

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")