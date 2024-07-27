import math
import itertools

# City coordinates
coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

num_cities = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate distances matrix
distances = {}
for i in range(num_cities):
    for j in range(num_cities):
        distances[(i, j)] = euclidean_distance(i, j)

# Implement a method to find a tour that minimizes the maximum distance between consecutive cities
def find_tour():
    # Start with a simple heuristic: nearest neighbour starting from the depot
    current_city = 0
    visit_order = [current_city]
    unvisited_cities = set(range(1, num_cities))

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: distances[(current_city, x)])
        visit_order.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    # Adding depot city to make a complete tour
    visit_order.append(0)

    # Calculate the total cost and max distance between consecutive cities
    total_cost = 0
    max_dist = 0
    for i in range(len(visit_order) - 1):
        dist = distances[(visit_order[i], visit_order[i+1])]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist

    return visit_order, total_cost, max_dist

# Retrieve the results
tour, total_travel_cost, maximum_distance = find_tour()

# Display solution
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", maximum_distance)