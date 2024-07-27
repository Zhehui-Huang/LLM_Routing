import math
from sys import maxsize
import itertools

# Define city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46),
    11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial city and setup
n = len(cities)
visited = set([0])
tour = [0]
current_city = 0
total_cost = 0

# Greedy nearest neighbor algorithm to construct initial solution
while len(visited) < n:
    next_city = min((i for i in range(n) if i not in visited), key=lambda i: distance(current_city, i))
    tour.append(next_city)
    visited.add(next_city)
    total_cost += distance(current_city, next_city)
    current_city = next_city

# Close the tour by returning to the depot city
tour.append(0)
total_cost += distance(current_city, 0)

# Compute the maximum distance between consecutive cities in the tour
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))