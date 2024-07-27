import math
from itertools import permutations

# List of city coordinates with indices corresponding to city numbers
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
          (62, 26), (79, 31), (61, 90), (42, 49)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.dist(cities[city1], cities[city2])

# Generate initial tour using a naive approach (nearest neighbor heuristic)
def initial_tour():
    unvisited = list(range(1, len(cities)))
    current = 0
    tour = [0]
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # return to the depot
    return tour

# Calculate total travel cost of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate tour
tour = initial_tour()
cost = total_distance(tour)

print("Tour:", tour)
print("Total travel cost:", cost)