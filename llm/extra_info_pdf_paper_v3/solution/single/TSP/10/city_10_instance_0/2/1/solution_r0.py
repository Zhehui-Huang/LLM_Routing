import math
from itertools import combinations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, cities):
    """Calculate the total travel cost for a given tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def nearest_neighbor_tour(start, cities):
    """Constructs a tour starting from the 'start' node using the nearest neighbor heuristic."""
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(start)  # Return to the depot
    return tour

# Define the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Generate a tour using the Nearest Neighbor heuristic
tour = nearest_neighbor_tour(0, cities)

# Calculate the total travel cost of the tour
total_cost = calculate_total_distance(tour, cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")