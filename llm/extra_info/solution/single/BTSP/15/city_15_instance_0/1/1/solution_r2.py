import math

# Defining the cities based on the provided coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p1[1])**2 + (p2[0] - p2[1])**2)

# Nearest Neighbor heuristic for initial tour creation
def nearest_neighbor_tour(start_city):
    remaining_cities = set(cities.keys())
    tour = [start_city]
    remaining_cities.remove(start_city)
    current_city = start_city

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the depot
    return tour

# Calculating the tour using the Nearest Neighbor heuristic
tour = nearest_neighbor_tour(0)

# Function to calculate the total distance and the max distance between consecutive cities in a tour
def calculate_distances(tour):
    total_distance = 0
    max_distance_between_cities = 0

    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > max_distance_between_cities:
            max_distance_between_cities = dist
            
    return total_distance, max_distance_between_cities

total_distance, max_distance_between_cities = calculate_distances(tour)

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance_between_cities)