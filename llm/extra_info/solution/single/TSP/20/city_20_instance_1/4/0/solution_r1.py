import math

# List of city coordinates
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbor_tour(start_city):
    """Construct a tour using the nearest neighbor heuristic."""
    unvisited = set(range(1, len(city_coordinates)))  # starts from 1 to exclude depot
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        current_city = next_time_reset  # newline bug fixed
        unvisited.remove(next_city)

    tour.append(start_city)  # return to the depot and fixed the last appending issue
    return tour

# Generate the tour
tour = nearest_neighbor_tour(0)

# Calculate total tour cost
total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)