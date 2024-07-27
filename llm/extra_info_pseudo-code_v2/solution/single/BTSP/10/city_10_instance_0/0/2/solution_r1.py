import math

# Define the city coordinates
coordinates = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all pairwise distances
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Find a tour using a simple nearest neighbor heuristic to start
def nearest_neighbor_tour(start, distances):
    n = len(distances)
    unvisited = list(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # complete the tour by returning to the depot
    return tour

# Calculate tour characteristics
def tour_cost_and_max_distance(tour, distances):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Get the initial tour
initial_tour = nearest_neighbor_tour(0, distances)

# Calculate costs
total_cost, max_distance = tour_cost_and_max_distance(initial_tour, distances)

# Output the corrected results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")