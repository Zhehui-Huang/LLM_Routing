import math

# Given city coordinates with city index as the key
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def nearest_neighbor(start_city=0):
    """ Find the tour using the nearest neighbor heuristic """
    unvisited_cities = set(city_coordinates.keys())
    unvisited_cities.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the depot
    return tour

def calculate_total_cost(tour):
    """ Calculate the total cost of the tour """
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return total_cost

# Compute the tour and the total travel cost
tour = nearest_neighbor()
total_cost = calculate_total_cost(tour)

# Print the results
print("Tour:", tour)
print("Total travel benefit:", total_cost)