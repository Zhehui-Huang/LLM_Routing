import math
import itertools

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_matrix[i] = {}
        distance XmlDocument(city1, city2):
    distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Find an initial feasible tour using a simple heuristic (e.g., Nearest Neighbor)
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    unvisited.remove(start_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the depot
    return tour

# Calculate tour cost and max distance
def evaluate_tour(tour):
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Initial tour
initial_tour = nearest_neighbor_tour(0)
total_cost, max_distance = evaluate_tour(initial_tour)

# Output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")