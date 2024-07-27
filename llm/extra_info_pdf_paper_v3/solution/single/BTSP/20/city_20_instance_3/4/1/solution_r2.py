import math

# Define the coordinates of the cities.
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two cities.
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate distances between all pairs of cities.
N = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(N)] for i in range(N)]

# Function to find a naive tour starting at the depot and using nearest neighbor heuristic.
def nearest_neighbor_tour(start=0):
    visited = set([start])
    tour = [start]
    current = start

    while len(visited) < N:
        next_city = min((city for city in range(N) if city not in visited), key=lambda x: distances[current][x])
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
    
    tour.append(start) # Return to the depot
    return tour

# Generate a naive tour
tour = nearest_neighbor_tour()

# Calculate the total travel cost and the maximum distance between consecutive cities in the tour.
total_travel_cost = 0
maximum_distance = 0
for i in range(1, len(tour)):
    dist = distances[tour[i-1]][tour[i]]
    total_travel_cost += dist
    if dist > maximum_distance:
        maximum_distance = dist

# Print the results in the required format
print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(maximum_distance, 2))