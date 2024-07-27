import math

# Definitions of cities
cities_coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the matrix of distances between all pairs of cities
num_cities = len(cities_coordinates)
distance_matrix = [
    [euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

def find_approx_tour():
    # Start at depot and find the nearest non-visited city until all cities are visited
    remaining_cities = list(range(1, num_cities))  # Exclude the depot city initially
    tour = [0]
    maximum_distance = 0

    while remaining_cities:
        last_city = tour[-1]
        next_city = min(remaining_cities, key=lambda x: distance_matrix[last_city][x])
        new_distance = distance_matrix[last_city][next_city]
        if new_distance > maximum_distance:
            maximum_distance = new_distance
        tour.append(next_city)
        remaining_cities.remove(next_city)

    # Completing the tour by returning to the depot
    final_distance_back = distance_matrix[tour[-1]][0]
    if final_distance_back > maximum_distance:
        maximum_distance = final_distance_back
    tour.append(0)

    # Calculating the total distance of the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]

    return tour, total_distance, maximum_distance

# Calculate approximate tour and its properties
tour, total_cost, max_distance = find_approx_tour()

# Output the required tour, total cost and max distance between consecutive cities
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")