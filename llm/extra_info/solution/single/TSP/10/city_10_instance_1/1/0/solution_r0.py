import math

# Coordinates of cities: city index maps to coordinate tuple (x, y)
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

# Function to calculate Euclidean distance between two cities given their coordinates
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating a distance matrix where the element at i, j is the Euclidean distance between city i and city j
num_cities = len(city_coords)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(city_coords[i], city_coords[j])
        else:
            distance_matrix[i][j] = float('inf')

# Nearest neighbor TSP algorithm
def nearest_neighbor_tsp(start_city):
    unvisited = set(range(num_cities))
    current_city = start_city
    tour = [current_city]
    unvisited.remove(current_city)
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        current_city = next city
        tour.append(current_city)
        unvisited.remove(current_city)

    # Return to start city
    total_cost += distance_matrix[current_city][start_city]
    tour.append(start_city)

    return tour, total_cost

# Calculate the shortest tour and total cost
tour, total_cost = nearest_neighbor_tsp(0)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)