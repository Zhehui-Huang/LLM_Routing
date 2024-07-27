import math

# Helper function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Coordinates of cities
cities = {
    0: (90, 3),  # depot city
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Simple TSP solver using the nearest neighbor strategy
def nearest_neighbor_tsp(start_city, cities):
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    unvisited_cities = list(cities.keys())
    unvisited_cities.remove(start_city)

    while unvisited_cities:
        nearest_city = None
        min_distance = float('inf')
        for city in unvisited_cities:
            distance = calculate_distance(cities[current_city], cities[city])
            if distance < min_distance:
                min_distance = distance
                nearest_city = city
        
        tour.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city
        unvisited_cities.remove(nearest_city)

    # Return to the starting city (Depot)
    return_distance = calculate_distance(cities[current_city], cities[start_city])
    tour.append(start_city)
    total_cost += return_distance

    return tour, total_cost

# Compute the TSP tour using the nearest neighbor heuristic
tour, total_cost = nearest_neighbor_tsp(0, cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")