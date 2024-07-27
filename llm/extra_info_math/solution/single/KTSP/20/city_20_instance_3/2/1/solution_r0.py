import math

# City coordinates indexed from 0 to 19
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the nearest city not yet visited
def find_nearest(current_city, visited):
    nearest_city = None
    min_dist = float('inf')
    for city in cities:
        if city not in visited:
            dist = distance(current_city, city)
            if dist < min_dist:
                min_dist = dist
                nearest_city = city
    return nearest_city, min_dist

# Function to solve the k-TSP problem using a modified nearest neighbor approach
def k_tsp_nearest_neighbor(start_city, k):
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    visited = set(tour)
    
    while len(tour) < k:
        next_city, dist = find_nearest(current_city, visited)
        tour.append(next_city)
        visited.add(next_city)
        total_distance += dist
        current_city = next_city
    
    # Closing the loop to return to the starting city
    back_to_start_dist = distance(current_city, start_city)
    tour.append(start_city)
    total_distance += back_to_start_dist
    
    return tour, total_distance

# Compute the k-TSP tour
tour_result, total_cost = k_tsp_nearest_neighbor(0, 13)
print("Tour:", tour_result)
print("Total travel cost:", total_cost)