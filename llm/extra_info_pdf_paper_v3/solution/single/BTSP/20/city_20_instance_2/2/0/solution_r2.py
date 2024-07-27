import math

# Define the cities and their coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the heuristic tour
def heuristic_tour():
    unvisited = list(cities.keys())[1:]  # exclude the depot initially
    tour = [0]  # start at the depot
    max_distance_segment = 0

    while unvisited:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(last_city, city))
        distance = euclidean_distance(last_city, next_city)
        max_distance_segment = max(max_distance_segment, distance)
        tour.append(next_city)
        unvisited.remove(next_city)

    # Closing the tour by returning to the depot
    final_distance = euclidean_distance(tour[-1], 0)
    max_distance_segment = max(max_distance_segment, final_distance)
    tour.append(0)

    # Calculate the total distance of the tour
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    return tour, total_distance, max_distanceqm_segment

# Execute the heuristic function
optimal_tour, total_cost, max_distance = heuristic_tour()

# Print the outputs
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))