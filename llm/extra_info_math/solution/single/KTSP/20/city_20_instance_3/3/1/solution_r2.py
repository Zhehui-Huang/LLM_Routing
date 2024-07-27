import itertools
from math import sqrt

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (30, 56),  # City 0: Depot
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Nearest neighbor heuristic to generate an initial feasible tour
def nearest_neighbor(cities, start_city, k):
    tour = [start_city]
    unvisited = set(range(len(cities)))
    unvisited.remove(start_city)
    
    while len(tour) < k:
        last_visited = tour[-1]
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[last_visited], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start_city)  # Return to the starting city
    return tour

# Calculate the total distance of a tour
def calculate_tour_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i - 1]]) for i in range(1, len(tour)))

# Find an initial tour with exactly 13 cities
initial_tour = nearest_neighbor(cities, 0, 13)
tour_distance = calculate_tour_distance(initial_tour, cities)

# Output the results
print("Tour:", initial_tour)
print("Total travel cost:", tour_distance)