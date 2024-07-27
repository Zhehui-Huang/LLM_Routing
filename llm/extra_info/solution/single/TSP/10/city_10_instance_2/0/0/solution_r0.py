import math
from itertools import permutations

def calculate_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(route, points):
    """ Calculate the total distance of the tour """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(points[route[i]], points[route[i+1]])
    return total_distance

def find_shortest_tour(points):
    n = len(points)
    # Generate all permutations of city indices, starting from 1 to n-1 (ignoring the depot city at index 0).
    all_routes = permutations(range(1, n))
    min_distance = float('inf')
    best_route = None
    for route in all_routes:
        # Consider the route starting and ending at the depot city
        current_route = [0] + list(route) + [0]
        current_distance = calculate_total_distance(current_route, points)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_route
    return best_route, min_distance

# City coordinates with Depot at index 0
city_coordinates = [
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

# Finding the shortest tour
tour, total_cost = find_shortest_tour(city_coordinates)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)