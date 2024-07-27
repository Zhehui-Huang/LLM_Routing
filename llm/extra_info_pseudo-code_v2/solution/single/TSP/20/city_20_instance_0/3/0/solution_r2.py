import math

# Define city coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Functions to calculate Euclidean distance
def distance(c1, c2):
    dx = cities[c1][0] - cities[c2][0]
    dy = cities[c1][1] - cities[c2][1]
    return math.sqrt(dx*dx + dy*dy)

# Calculate distance matrix
dist_matrix = [[distance(i, j) for j in range(20)] for i in range(20)]

# Nearest Neighbor heuristic for a starting solution
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to the start city
    return tour

# Calculate total travel cost of the tour
def tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Create initial tour and calculate its cost
initial_tour = nearest_neighbor_tour(0)
cost = tour_cost(initial_tour)

# Output the results
print("Tour:", initial_tour)
print("Total travel cost:", cost)