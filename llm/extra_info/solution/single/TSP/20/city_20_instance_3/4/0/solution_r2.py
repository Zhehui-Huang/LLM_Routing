import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two city coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(cities):
    """Generate a tour starting at the depot city using the nearest neighbor heuristic."""
    num_cities = len(cities)
    unvisited = set(range(1, num_cities))  # Start from city 1 to the last, depot is city 0
    tour = [0]  # start the tour from the depot
    current_city = 0
    total_cost = 0

    # Continue till all cities are visited
    while unvisited:
        nearest_city = None
        min_distance = float('inf')

        for city in unvisited:
            distance = euclidean_distance(cities[current_city], cities[city])
            if distance < min_distance:
                min_distance = distance
                nearest_city = city

        tour.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to the depot to complete the circuit
    return_to_depot_distance = euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += return_to_depot_distance

    return tour, total_cost

# Coordinates for each city, including the depot
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Generate the tour
tour, total_cost = nearest_neighbor_tour(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)