import math
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Utility function to calculate Euclidean distance between two cities given their indices
def dist(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Heuristic: Nearest Neighbor Approach to minimize the max distance between consecutive cities
def nearest_neighbor_approach(cities, start=0):
    unvisited = set(cities.keys()) - {start}
    tour = [start]
    current_city = start
    max_edge_length = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist(x, current_city))
        max_edge_length = max(max_edge_length, dist(current_city, next_city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next, current_city[0]
    
    # Closing the tour by returning to the depot
    tour.append(start)
    max_edge_length = max(max_edge_length, dist(current_city, start))

    # Calculate the total cost of the tour
    total_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_edge_length

# Find the tour using nearest neighbor approach
tour, total_cost, max_distance = nearest_neighbor_approach(cities)

# Output the tour, total travel cost and maximum distance between consecutive cities
output = f"Tour: {tour}\nTotal travel cost: {total_cost}\nMaximum distance between consecutive cities: {max_distance}"
print(output)