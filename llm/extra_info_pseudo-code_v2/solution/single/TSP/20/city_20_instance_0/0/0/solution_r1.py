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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Nearest Neighbor Algorithm to find an initial solution
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # Return to the depot
    return tour

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cabs[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate the tour using the nearest neighbour heuristic and compute its cost
tour = nearest_neighbor_tour(0)
total_cost = calculate_tour_cost(tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)