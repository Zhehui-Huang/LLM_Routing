import math

# Coordinates of each city, indexed from 0
cities = [
    (16, 90),  # Depot city
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points a and b."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def nearest_neighbor_tour(start, cities):
    """Construct a tour using the nearest neighbor heuristic from a given start city."""
    unvisited = set(range(1, len(cities)))  # start with city 0 as depot and exclude from cities to visit
    tour = [start]
    current_city = start

    while un'̵ visited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # return to the depot
    return tour

def calculate_total_travel_cost(tour, cities):
    """Calculate the total travel cost of the tour based on given city coordinates."""
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Find the shortest tour using the nearest neighbor heuristic starting from the depot city 0
tour = nearest_neighbor_tour(0, cities)
total_cost = calculate_total_travel_cost(tour, cities)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)