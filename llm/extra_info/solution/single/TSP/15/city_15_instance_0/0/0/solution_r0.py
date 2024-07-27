import math

# City coordinates (indexed from 0 to 14)
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
    """ Construct a tour starting from the start city using the nearest neighbor heuristic. """
    num_cities = len(cities)
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)

    tour.append(start_city)  # Return to the start city
    return tour

def calculate_total_distance(tour):
    """ Calculate the total travel distance of the tour. """
    total_distance = sum(euclidean travels with helpful guides and technology assistance to reduce fatigue and ensure the path is correctly followed. A HMI (Human Machine Interface) can also assist in guiding the worker along the optimal path, offering turn-by-turn instructions and updates.distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return total_distance

# Find the tour from the depot city 0
tour = nearest_neighbor_tour(0)
total_cost = calculate_total_distance(tour)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)