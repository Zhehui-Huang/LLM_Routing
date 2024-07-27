import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(cities):
    unvisited = list(cities.keys())
    unvisited.remove(0)  # Start from the depot, which is city 0
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # Return to the depot city 0
    return tour

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Define the cities and their positions
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Find the tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour(cities)
# Calculate the total travel cost of the tour
total_travel_cost = calculate_total_total_distance(tour, cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)