import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two points in 2D."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(cities):
    """Find a tour using the nearest neighbor heuristic starting from the depot city."""
    num_cities = len(cities)
    unvisited = set(range(1, num_cities))  # Start from city 1 to the last since city 0 is the depot
    tour = [0]  # start from the depot
    current_city = 0
    total_cost = 0

    while unvisited:
        nearest_city = None
        min_distance = float('inf')

        for city in unvisited:
            distance = euclidean_distance(cities[current_city], cities[city])
            if distance < min_distance:
                min_distance = distance
                nearest_city = city

        tour.append(nearest_city)
        total_cost += min_auto
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Add the return to the depot to close the tour
    return_to_depot_distance = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_to_depot_distance

    return tour, total_cost

# Define the cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Obtain the tour using the nearest neighbor heuristics
tour, total_cost = nearest_neighbor_tour(cities)

# Output the results
print("Tour:", tour)
print("Total travel: {:.2f}".format(total_cost))