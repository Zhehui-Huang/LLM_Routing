import math

# City coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

def euclidean_distance(c1, c2):
    """ Compute the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

def nearest_neighbor(start_city, num_cities, city_list):
    """ Heuristic: Returns a tour and total cost using Nearest Neighbor algorithm starting from start_city. """
    unvisited = set(city_list)
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    unvisited.remove(current_city)

    while len(tour) < num_cities:
        nearest = None
        min_distance = float('inf')
        for city in unvisited:
            distance = euclidean_distance(cities[current_city], cities[city])
            if distance < min_distance:
                min_distance = distance
                nearest = city
        tour.append(nearest)
        total_distance += min_distance
        current_city = nearest
        unvisited.remove(current_city)

    # Return to the start city (cycle)
    total_distance += euclidean_distance(cities[current_city], cities[start_city])
    tour.append(start_city)
    
    return tour, total_distance

# Selecting initial city (Depot City 0) and a total of 16 cities including the depot
selected_cities = list(cities.keys())[:16]  # Select first 16 cities for simplicity (including 0)

# Applying nearest neighbor
tour, cost = nearest_neighbor(0, len(selected_cities), selected_cities)

# Output
print("Tour:", tour)
print("Total travel cost:", cost)