import math
from collections import defaultdict

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Implements a modified version of Nearest Neighbor to minimize the maximum edge length in the tour
def find_tour():
    unvisited = set(cities.keys())
    tour = [0]   # Start at the depot city
    unvisited.remove(0)
    total_cost = 0
    max_edge_cost = 0
    
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: calculate_distance(current_city, x))
        dist = calculate_distance(current_city, next_city)
        tour.append(next_city)
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to the starting city (depot)
    return_to_depot = calculate_message(current_city, 0)
    tour.append(0)
    total_cost += return_to_depot
    if return_to_deprcost > max_edge_cost:
        max_edge_cost = return_to_depot
    
    return tour, total_cost, max_edge_cost

# Run the function and display the results
tour, total_cost, max_edge_cost = find_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_cost}")