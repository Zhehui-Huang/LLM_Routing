import numpy as np

# Coordinates of the cities including the depot city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Number of cities
num_cities = len(coordinates)

# Calculate the Euclidean distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Function to calculate the total tour length
def calculate_tour_length(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Select one city from each group to minimize the cost from the depot
def select_cities_from_groups(groups, depot_index, distance_matrix):
    selected_cities = [depot_index]  # start at the depot
    for group in groups:
        min_city = None
        min_cost = float('inf')
        for city in group:
            round_trip_cost = distance_matrix[depot_index, city] + distance_matrix[city, depot_index]
            if round_trip_cost < min_cost:
                min_cost = round_trip_cost
                min_city = city
        selected_cities.append(min_city)
    selected_cities.append(depot_index)  # end at the depot
    return selected_cities

selected_cities = select_cities_from_groups(city_groups, 0, distance_matrix)

# Simple heuristic: sort selected cities (excluding the depot) by minimizing travel cost
# Starting from the first city in selected cities after the depot
def heuristic_tour(selected_cities, distance_matrix):
    current_city = selected_cities[1]
    tour = [0, current_city]
    remaining_cities = set(selected_cities[2:-1])
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distance_matrix[current_city, x])
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    
    tour.append(0)  # Return to depot
    return tour

# Get the tour using the heuristic
tour = heuristic_tour(selected_cities, distance_matrix)
tour_cost = calculate_tour_length(tour, distance_matrix)

# Output results
print("Tour:", tour)
print("Total travel cost:", tour_cost)