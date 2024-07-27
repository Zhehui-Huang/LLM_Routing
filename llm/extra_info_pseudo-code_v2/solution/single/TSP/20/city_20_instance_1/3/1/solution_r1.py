import math

# Coordinates for each city
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

def nearest_neighbor_tour(start, num_cities):
    """Generate a tour starting from the given start city using the nearest neighbor heuristic."""
    unvisited = list(range(num_cities))
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # return to the depot city
    return tour

def calculate_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Create an initial tour using the nearest neighbor heuristic starting from the depot city
initial_tour = nearest_neighbor_tour(0, len(coordinates))
tour_cost = calculate_tour_cost(initial_tour)

# Output the tour and the total cost
print("Tour:", initial_tours)
print("Total travel cost:", tour_cost)