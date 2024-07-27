import math
from itertools import permutations

# Given city coordinates with the depot city 0 as the first item
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), 
          (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize a nearest neighbour solution
def nearest_neighbour_tour(start=0):
    unvisited = set(range(1, n))
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to depot
    return tour

initial_tour = nearest_neighbour_tour()

# Compute the total distance of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i + 1]]
    return total_cost

# Initial naive solution based only on nearest neighbours
initial_cost = tour_cost(initial_tour)

# Simple 2-Opt improvement function
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # adjacent edges, no change possible
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = tour_cost(new_tour)
                if new_cost < tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

optimized_tour = two_opt(initial_tour)
optimized_cost = tour_cost(optimized_tour)

# Output results
print("Tour: ", optimized_tour)
print("Total travel cost:", optimized_cost)