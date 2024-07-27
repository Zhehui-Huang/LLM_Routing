import math
import itertools

# Helper function to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# List of cities with their coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities to select including the depot (k total, including depot)
k = 13

# Simple heuristic: Start at the depot and find nearest unvisited city until k cities are visited
def select_cities(cities, k):
    visited = [0]  # Start from depot
    while len(visited) < k:
        last_visited = visited[-1]
        nearest_city = None
        min_distance = float('inf')
        for i in range(len(cities)):
            if i not in visited:
                distance = euclidean_distance(cities[last_visited], cities[i])
                if distance < min_distance:
                    nearest_city = i
                    min_distance = distance
        visited.append(nearest_city)
    return visited

# Generate all permutations of the selected cities and choose the shortest path
def find_shortest_tour(selected_cities):
    shortest_path = None
    min_cost = float('inf')
    for order in itertools.permutations(selected_cities):
        # Ensure the tour starts and ends at the depot (city index 0)
        if order[0] == 0 and order[-1] == 0:
            current_cost = sum(euclidean_distance(cities[order[i]], cities[order[i+1]]) for i in range(len(order) - 1))
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_path = order
    return shortest_path, min_cost

selected_city_indices = select_cities(cities, k)
selected_cities_order, total_cost = find_shortest_tour(selected_city_indices + [0])  # Re-add depot to the end for round trip

# Output the results
print("Tour:", list(selected_cities_order))
print("Total travel cost:", total_cost)