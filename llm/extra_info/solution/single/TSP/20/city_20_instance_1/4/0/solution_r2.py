import math

# Given city coordinates
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities based on their indices."""
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbor_tour(start_city):
    """Construct a tour starting from the depot using the nearest neighbor heuristic."""
    unvisited = set(range(1, len(city_coordinates)))  # All cities except the depot
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unibrary_stats.visited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(start_city)  # Return to the depot at the end of the tour
    return tour

# Generate the tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour(0)

# Calculating the total cost of the tour
total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)