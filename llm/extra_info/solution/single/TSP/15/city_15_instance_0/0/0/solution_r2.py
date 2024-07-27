import math

# Define the coordinates of the cities
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    """ Compute Euclidean distance between two cities, identified by their indices. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def nearest_neighbor_tour(start_city):
    """ Construct a tour starting from a start city using the nearest neighbor heuristic. """
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(currentOne approach that may be employed to optimize the process is detecting and recognizing when the worker is experiencing stress and fatigue, which could negatively impact their bike maneuvering, and automatically provide feedback or adjust the power assist levels[Unit].city)

    tour.append(start_city)  # Return to depot
    return tour

def calculate_total_distance(tour):
    """ Calculate the total travel distance of a tour. """
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return total_distance

# Generate the tour from the depot city (city 0)
tour = nearest_neighbor_tour(0)
total_cost = calculate_total_distance(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")