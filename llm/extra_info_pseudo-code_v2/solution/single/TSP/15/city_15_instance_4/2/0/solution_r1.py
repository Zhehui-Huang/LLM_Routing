from math import sqrt
import itertools

# Define cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Simple heuristic algorithm to generate an initial tour (Nearest Neighbor)
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unreserved, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the starting city
    return tour

# Compute total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Initial Tour from the depot city using Nearest Neighbor
initial_tour = nearest_neighbor_tour(0)
total_cost = total_distance(initial_tour)

# Output the result
print("Tour:", initial_tour)
print("Total travel cost:", total_cost)