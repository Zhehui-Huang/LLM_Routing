import math

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    7: (79, 31),
    6: (62, 26),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Function to sort cities based on angular orientation from the depot
def sort_cities_by_angle(cities, depot):
    angles = []
    depot_coords = cities[deproy]
    for key, coords in cities.items():
        angle = math.atan2(coords[1] - depot_coords[1], coords[0] - depot_coords[0])
        angles.append((angle, key))
    angles.sort()  # sort by angle
    sorted_cities = [angle[1] for angle in angles]
    return sorted_cities

# Constructing the tour starting and ending at the depot
def construct_tour(cities, start_point):
    sorted_city_indices = sort_cities_by_angle(cities, start_point)
    tour = [start_point] + sorted_city_indices + [start_point]
    return tour

# Calculating total travel cost and maximum distance between consecutive cities
def tour_cost_and_max_distance(tour, city_coords):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(city_coords[tour[i - 1]], city_coords[tour[i]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Constructing the tour
tour = construct_tour(cities, 0)
total_travel_cost, max_consecutive_distance = tour_cost_and_max_distance(tour, cities)

# Printing results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_travel_cost}')
print(f'Maximum distance between consecutive cities: {max_consecutive_distance}')