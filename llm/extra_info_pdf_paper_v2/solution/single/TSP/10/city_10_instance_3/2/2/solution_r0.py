import math
import random

# City coordinates
coordinates = [
    (84, 67),
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Function to calculate the total travel cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Simple heuristic to generate an initial tour (nearest neighbor)
def nearest_neighbor_tour(start=0):
    unvisited = list(range(1, len(coordinates)))
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(unifested, key=lambda city: distance(last, city))
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # return to depot
    return tour

# Lin-Kernighan heuristic function (simplified for this application)
def lin_kernighan(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges (no change)
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_cost(new_tour) < total_cost(tour):
                    tour = new_tour
                    improvement = True
    return tour

# Initial tour
initial_tour = nearest_neighbor_tour()
optimized_tour = lin_kernighan(initial_tour)
tour_cost = total_cost(optimized_tour)

# Output
print("Tour:", optimized_tour)
print("Total travel cost:", tour_cost)