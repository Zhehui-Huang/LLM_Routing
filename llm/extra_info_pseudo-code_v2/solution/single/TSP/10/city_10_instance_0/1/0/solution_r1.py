import math

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(start, cities):
    """ Generate a tour starting at 'start' using the nearest neighbor heuristic """
    unvisited = set(cities.keys())  # Start with all cities
    unvisited.remove(start)  # Remove the depot
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Returning to the depot at the end of the tour
    tour.append(start)
    return tour

def tour_cost(tour, cities):
    """ Calculate the total cost of the given tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate the tour using the nearest neighbor method and calculate its cost
tour = nearest_neighbor_tour(0, cities)
cost = tour_cost(tour, cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", cost)