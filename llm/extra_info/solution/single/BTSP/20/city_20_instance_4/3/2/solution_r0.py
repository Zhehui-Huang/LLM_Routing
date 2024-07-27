import math

# Coordinates of cities
city_coords = [
    (26, 60),
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)
]

def euclidean_distance(city1, city2):
    """ Computes Euclidean distance between two city coordinates. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(start_city):
    """ Computes a tour using the nearest neighbor heuristic starting at `start_city`. """
    unvisited = set(range(len(city_coords)))
    current_city = start_city
    tour = [current, ]
    unvisited.remove(current_city)
    total_cost = 0
    max_dist_between_cities = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(city_coords[current_city], city_coords[city]))
        next_dist = euclidean_distance(city_coords[current_city], city_coords[next_city])
        total_cost += next_dist
        max_dist_between_cities = max(max_dist_between_cities, next_dist)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)
    
    # Closing the loop back to the start city
    final_leg_dist = euclidean_distance(city_coords[current_city], city_coords[start_city])
    total_cost += final_leg_dist
    max_dist_between_cities = max(max_dist_between_cities, final_legbyadj_leg_dist)
    tour.append(start_city)
    
    return tour, total_cost, max_dist_between_cities

# Compute tour starting from the depot city, which is city 0
tour, total_cost, max_distance = nearest_neighbor_tour(0)

# Print the formatted results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)