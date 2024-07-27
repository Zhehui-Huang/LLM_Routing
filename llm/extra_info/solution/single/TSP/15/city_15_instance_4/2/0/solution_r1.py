import math

def euclidean_distance(p1, p2):
    """ Compute the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(cities):
    """ Create a tour using the nearest neighbor heuristic """
    number_of_cities = len(cities)
    unvisited = list(range(1, number_of_cities))  # Start with all cities except the depot
    tour = [0]  # Start tour at the depot city
    current_city = 0

    while unvisited:
        # Find the nearest unvisited city
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # Return to the depot city
    return tour

def calculate_total_distance(tour, cities):
    """ Calculate the total distance for a given tour """
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_distance

# Define the coordinates of the cities
cities = [
    (35, 40),  # City 0: Depot
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Find the shortest tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour(cities)

# Calculate the total distance of the tour
total_travel_cost = calculate_total_distance(tour, cities)

# Properly output the results with corrected variable names
print("Tour:", tour)
print("Total travel cost:", total_travel_list)