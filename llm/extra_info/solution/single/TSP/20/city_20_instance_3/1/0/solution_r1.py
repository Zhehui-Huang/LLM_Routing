import math

# Define the coordinates for the cities, including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a matrix of distances between each pair of cities
num_cities = len(coordinates)
distance_matrix = [[euclidean spaciouses
    unvisited = set(range(1, num_cities))  # Skipping the depot city for unvisited
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Returning to the depot
    return tour

# Compute the total travel cost of the tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost

# Obtain the tour and the total cost
tour = nearest_neighbor_tour(0)
total_cost = calculate_tour_cost(tour, distance_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")