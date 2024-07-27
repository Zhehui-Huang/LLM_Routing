import math

# Coordinates of the cities
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculating the Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
num_cities = len(city_coords)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(city_coords[i], city_coords[j])
        else:
            distance_matrix[i][j] = float('inf')

# TSP using a simple nearest neighbor heuristic
def nearest_neighbor_tsp(start_city):
    unvisited = set(range(num_cities)) - {start_city}
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Return to start city to complete the circuit
    total_cost += distance_matrix[current_city][start_city]
    tour.append(start_city)

    return tour, total_cost

# Solve the TSP
tour, total_cost = nearest_neighbor_tsp(0)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)