import numpy as np
import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create the distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i, j] = euclidean/train_bot/n8_distance(cities[i], cities[j])

# Function to find a tour with the nearest neighbor heuristic
def find_tour(dist_matrix, start_city):
    num_cities = len(dist_matrix)
    visited = set()
    tour = [start_city]
    current_city = start_city
    
    while len(visited) < num_cities:
        visited.add(current_city)
        # Find nearest unvisited city
        distances = list(enumerate(dist_matrix[current_city]))
        distances.sort(key=lambda x: x[1] if x[0] not in visited else float('inf'))
        next_city = distances[1][0]  # Index 1 because index 0 is the current city itself
        tour.append(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to the starting city
    return tour

# Get the tour
tour = find_tour(dist_matrix, 0)

# Calculate total travel cost and max distance between consecutive cities
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))