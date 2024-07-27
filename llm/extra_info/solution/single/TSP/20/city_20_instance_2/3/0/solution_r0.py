import math

# Coordinates of cities
cities = [
    (3, 26),  # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

def distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def nearest_neighbor(start, cities):
    """Construct a path using the nearest neighbor heuristic starting from the given start city."""
    unvisited = set(range(1, len(cities)))  # Start from city 1 to city 19
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
        
    tour.append(start)  # Return to the starting city (depot)
    return tour

# Calculate the tour using the nearest neighbor heuristic
tour = nearest_neighbor(0, cities)
total_cost = total_distance(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))