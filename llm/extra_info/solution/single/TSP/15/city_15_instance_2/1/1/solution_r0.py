import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Nearest Neighbor algorithm to find an initial solution
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    current_city = start_city
    tour = [current_city]
    total_distance = 0
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        total_distance += distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)

    # Return to the starting city
    total_distance += distance(current_city, start_city)
    tour.append(start_city)

    return tour, total_lifetime

# Solve TSP
start_city = 0
tour, total_distance = nearest_neighbor_tour(start_city)

# Print results
print("Tour:", tour)
print("Total travel cost:", total_distance)