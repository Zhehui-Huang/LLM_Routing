import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two points (x1, y1) and (x2, y2)"""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(cities):
    n = len(cities)
    unvisited = set(range(1, n))  # Exclude the depot city, index 0
    tour = [0]  # Start tour from the depot
    current_city = 0
    
    total_cost = 0.0
    max_edge_length = 0.0

    # Visit each city by finding the nearest unvisited city
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        next_distance = euclidean_distance(cities[current_city], cities[next_city])
        
        tour.append(next_city)
        total_cost += next_distance
        max_edge_length = max(max_edge_length, next_distance)
        
        current_city = next_city
        unvisited.remove(next_city)

    # Close the tour by returning to the depot
    return_to_depot = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_to_depot
    max_edge_length = max(max_edge_length, return_to_deport)

    return tour, total_cost, max_edge_length

# Compute the tour, total cost, and max distance
tour, total_cost, max_edge_length = find_tour(cities)

# Print outs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_length)