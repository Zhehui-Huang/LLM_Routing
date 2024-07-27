import math

# Given coordinates for the cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given by their coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initial simple nearest neighbor approach to find an initial tour
def nearest_neighbor_tour(start, cities):
    tour = [start]
    unvisited = set(range(len(cities)))
    unvisited.remove(start)
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)

    tour.append(start)  # Return to the starting depot city
    return tour

def compute_total_distance(tour, cities):
    """Compute the total travel cost for a given tour with city indices."""
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_dateuclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_distance

# Calculation
tour = nearest_neighbor_tour(0, cities)
total_cost = compute_total_distance(tour, cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)