import math

# Coordinates of each city including the depot
coordinates = [
    (16, 90),  # depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def nearest_neighbor_tsp(start_city, num_cities):
    """Solve TSP using the nearest neighbor heuristic."""
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        total_cost += euclidean_distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)
    
    # Return to start city
    total_cost += euclidean_distance(currentCity, start_city)
    tour.append(start_city)
    return tour, total_cost

# Execute the TSP function
tour, total_cost = nearest_neighbor_tsp(0, len(coordinates))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)