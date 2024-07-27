import math

# City coordinates (index corresponds to the city number)
cities = [
    (8, 11),   # Depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 19)
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(start_index):
    """ Construct a tour starting from the specified index using the nearest neighbor heuristic. """
    num_cities = len(cities)
    to_visit = set(range(num_cities))
    tour = [start_index]
    to_visit.remove(startance(city1, city_index)

    while to_visit:
        next_city = min(to_visit, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        to_visit.remove(next_city)
        current_city = next_city

    tour.append(start_index)  # Return to the depot
    return tour

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of a tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Calculate the tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour(0)
total_cost = calculate_tour_cost(tour)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)