import math
from random import sample

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def calculate_total_cost(tour, coordinates):
    """Calculate total cost for a given tour by summing the distances between consecutive cities in the tour."""
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def nearest_neighbor_solution(start, cities, coordinates):
    """Generates a tour starting and ending at the start point using the nearest neighbor heuristic."""
    if not cities:
        return [start, start]
    tour = [start]
    current = start
    to_visit = set(cities)
    while to_visit:
        next_city = min(to_visit, key=lambda city: euclidean_distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        to_visit.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Constants and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
num_robots = 2
depot = 0
cities = list(range(1, 21))  # Cities excluding the depot

# Generate an initial tour by dividing cities approximately equally among the robots
split_size = len(cities) // num_robots
tours = []

# Create initial tours
for i in range(num_robots):
    start = i * split_size
    end = (i + 1) * split_size if i < num_robots - 1 else len(cities)
    partial_cities = cities[start:end]
    tour = nearest_neighbor_solution(depot, partial_cities, coordinates)
    tours.append(tour)

# Calculate tour costs
tour_costs = [calculate_total_custocities)]
maximum_cost = max(tour_costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {maximum_cost}")