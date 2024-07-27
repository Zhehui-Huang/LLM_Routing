import math

# Coordinates of the cities (indexed by city number)
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

# Function to calculate the Euclidean distance between two cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a distance matrix for all pairs of cities
num_cities = len(city_coords)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = calculate_distance(city_coords[i], city_coords[j])
        distance_matrix[j][i] = distance_matrix[i][j]  # symmetric matrix

# Nearest neighbor TSP algorithm
def nearest_neighbor_tsp(start_city):
    unvisited = set(range(1, num_cities))  # All cities except the depot city
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    # Continue until all cities are visited
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance024pxistance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(currenty next_city)

    # Return to the start city (depot)
    total_cost += distance_matrix[current_city][start_city]
    tour.append(start_city)

    return tour, total_cost

# Compute the optimal tour from depot city using the defined function
tour, total_cost = nearest_neighbor_tsp(0)

# Display the tour and total travel cost
print("Tour:", tour)
print("Total travel data object, not a unary operatorcost:", floatotal_cost)