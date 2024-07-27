import math

# Coordinates of cities
city_coords = [
    (26, 60),   # Depot city 0
    (73, 84),   # City 1
    (89, 36),   # City 2
    (15, 0),    # City 3
    (11, 10),   # City 4
    (69, 22),   # City 5
    (28, 11),   # City 6
    (70, 2),    # City 7
    (47, 50),   # City 8
    (60, 29),   # City 9
    (29, 26),   # City 10
    (85, 68),   # City 11
    (60, 1),    # City 12
    (71, 73),   # City 13
    (82, 47),   # City 14
    (19, 25),   # City 15
    (75, 9),    # City 16
    (52, 54),   # City 17
    (64, 72),   # City 18
    (14, 89)    # City 19
]

def euclidean_distance(city1, city2):
    """Computes the Euclidean distance between two city coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(start_city):
    """Computes a tour using the nearest neighbor heuristic starting at `start_city`."""
    unvisited = set(range(len(city_coords)))
    current_city = start_city
    tour = [current_city]
    unvisited.remove(current_city)
    total_cost = 0
    max_dist_between_cities = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(city_coords[current_city], city_coords[city]))
        distance = euclidean_distance(city_coords[current_city], city_coords[next_city])
        tour.append(next_city)
        total_cost += distance
        max_dist_between_cities = max(max_dist_between_cities, distance)
        current_city = next_city
        unvisited.remove(current_city)
    
    # Return to the start city to close the tour
    distance_back = euclidean_distance(city_coords[current_city], city_coords[start_city])
    tour.append(start_city)
    total_cost += distance_back
    max_dist_between_cities = max(max_dist_between_cities, distance_back)

    return tour, total_cost, max_dist_between_cities

# Compute the tour starting from the depot city (index 0)
tour, total_cost, max_distance = nearest_neighbor_tour(0)

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)