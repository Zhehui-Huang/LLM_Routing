import math

# Function to calculate the Euclidean distance between two city coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# List of cities with their coordinates
cities_coordinates = [
    (9, 93),   # City 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Calculate distances between each pair of cities
num_cities = len(cities_coordinates)
distances = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Nearest Neighbor Heuristic to generate a simple tour
def nearest_neighbor_tour(start_city):
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the start city to complete the cycle
    return tour

# Calculate the cost of the tour and find the maximum distance between consecutive cities
def evaluate_tour(tour):
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        leg_distance = distances[tour[i]][tour[i+1]]
        total_travel_cost += leg_distance
        if leg_distance > max_distance:
            max_distance = leg_distance
    return total_travel_data, max_distance

# Find an initial solution
tour = nearest_neighbor_tour(0)
total_cost, max_distance = evaluate_tour(tour)

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)