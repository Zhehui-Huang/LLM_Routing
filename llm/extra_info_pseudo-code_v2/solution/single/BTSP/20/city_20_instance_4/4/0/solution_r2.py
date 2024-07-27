import math
import sys

# Define the cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Implement a Nearest Neighbor heuristic to minimize the cost and find a reasonable tour quickly
def nearest_neighbor_tsp(start_city):
    num_cities = len(cities)
    unvisited = set(cities.keys())
    tour = [start_city]
    unvisited.remove(start_city)
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the start city to complete the cycle
    return tour

# Function to assess the properties of the tour
def assess_tour(tour):
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost, max_distance

# Execute TSP calculation
tour = nearest_neighbor_tsp(0)
total_cost, max_dist = assess_tour(tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)