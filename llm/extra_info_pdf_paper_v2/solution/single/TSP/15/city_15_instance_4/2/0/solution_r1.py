import math
import random

# City coordinates indexed by city number
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate the Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Building an initial solution using a simple nearest neighbor approach
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # returning to the depot
    return tour

# Calculate the total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Implement Lin-Kernighan Heuristic
def lin_kernighan(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                L1, L2 = tour[i:i + 2], tour[j:j + 2]
                if distance(*L1) + distance(*L2) > distance(L1[0], L2[0]) + distance(L1[1], L2[1]):
                    tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]  # reverse section of the tour
                    improved = True
    return tour

# Solving the TSP
start = 0
initial_tour = nearest_neighbor_tour(start)
optimized_tour = lin_kernighan(initial_tour)
total_distance = tour_cost(optimized_tour)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_distance)