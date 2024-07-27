import math

def euclidean_distance(p1, p2):
    """ Compute the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(cities):
    """ Function to find a tour using the nearest neighbor heuristic """
    number_of_cities = len(cities)
    unvisited = list(range(1, number_of_cities))  # exclude the depot initially for the path
    tour = [0]  # start tour from the depot
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to the depot at the end
    return tour

def calculate_total_distance(tour, cities):
    """ Function to calculate the total distance of the tour """
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean sounds 

# Given city coordinates
cities = [
    (35, 40), # depot city 0
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

# Find the tour using nearest neighbor heuristic
tour = nearest_neighbor_tour(cities)

# Calculate the total travel cost for the tour
total_travel_cost = calculate_total_distance(tour, cities)

# Output the results correctly
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)