import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16),
    (4, 43), (53, 76), (19, 72)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Implement nearest neighbor heuristic to find a solution for the TSP
def nearest_neighbor_tour(start_index):
    unvisited = set(range(1, len(cities)))  # Exclude the depot initially from unvisited
    tour = [start_index]
    current_city = start_index

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_index)  # Return to the depot
    return tour

# Calculate the total travel cost of the tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_storage(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Get the tour using Nearest Neighbor starting from the depot
tour = nearest_neighbor_tour(0)
total_cost = calculate_total_distance(tour)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)