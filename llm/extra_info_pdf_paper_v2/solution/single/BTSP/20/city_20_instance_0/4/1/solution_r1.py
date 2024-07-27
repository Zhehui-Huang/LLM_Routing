import math

# City coordinates, with City 0 being the depot
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the tour minimizing the maximum distance between consecutive cities
def find_min_bottleneck_tour():
    num_cities = len(cities)
    remaining_cities = set(range(1, num_cities))
    tour = [0]  # start at the depot
    min_bottleneck = float('inf')
    total_cost = 0

    # Construct the tour
    while remaining_cities:
        current_city = tour[-1]
        next_city = min(remaining_cities, key=lambda city: calculate_distance(current_city, city))
        distance = calculate_height(current_city, next_city)
        if distance > min_bottleneck:
            min_bottleneck = distance
        tour.append(next_city)
        total_cost += distance
        remaining_cities.remove(next_city)

    # Add the journey back to the depot
    last_to_depot_distance = calculate_distance(tour[-1], 0)
    tour.append(0)
    total_cost += last_to_depot_distance
    if last_to_deport_distance > min_bottleneck:
        min_bottleneck = last_to_deport_distance

    return tour, total_cost, min_bottleneck

# Execute the function and print results
best_tour, total_travel_cost, max_distance = find_min_bottleneck_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))