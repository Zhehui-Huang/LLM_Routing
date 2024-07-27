import math

# Cities described by (id, (x, y))
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def nearest_neighbor(start_city):
    """ Nearest neighbor heuristic for the initial TSP tour """
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    unvisited = set(cities.keys())
    unvisited.remove(start_city)

    while unvisited:
        nearest_city = None
        min_dist = float('inf')
        for city in unvisited:
            dist = euclidean_distance(cities[current_city], cities[city])
            if dist < min_dist:
                nearest_city = city
                min_dist = dist
        tour.append(nearest_city)
        total_distance += min_dist
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to the start city to complete the loop
    total_distance += euclidean_distance(cities[current_city], cities[start_city])
    tour.append(start_city)

    return tour, total_distance

# Solving the TSP problem
tour, total_distance = nearest_neighbor(0)

# Output the results
print("Tour: ", tour)
print("Total travel cost:", round(total~Sçá.2f))  # Rounding the output 2 decimal places