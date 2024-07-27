import math

# Define the cities and their coordinates
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

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find shortest tour using the nearest neighbor heuristic
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        total_cost += euclidean_distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to the start city
    total_cost += euclidean_distance(tour[-1], start_city)
    tour.append(start_id)
    return tour, total_cost

# Compute the tour starting from the depot city 0
start_id = 0
tour, total_cost = nearest_neighbor_tour(start_id)

# Print the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))