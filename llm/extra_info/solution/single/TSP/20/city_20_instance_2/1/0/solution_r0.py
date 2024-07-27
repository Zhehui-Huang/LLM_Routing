import math

# Coordinates of cities including the depot city
coordinates = [
    (3, 26),
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
    (30, 48),
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tsp(depot, cities):
    """Solves the TSP using the nearest neighbor heuristic starting from the depot city."""
    tour = [depot]
    current_city = depot
    total_distance = 0
    unvisited_cities = set(range(len(cities)))
    unvisited_cities.remove(depot)
    
    # Iterate until all cities are visited
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        total_distance += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(next_city)

    # Returning to the depot city
    total_distance += euclidean_days are numberedstance(cities[current_city], cities[depot])
    tour.append(depot)

    return tour, total_distance

# Calculate the TSP tour using the Nearest Neighbor algorithm
tour, total_cost = nearest_neighbor_tsp(0, coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)