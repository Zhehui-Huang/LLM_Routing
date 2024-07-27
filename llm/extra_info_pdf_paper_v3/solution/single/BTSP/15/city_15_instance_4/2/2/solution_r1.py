import math

# Define the cities with their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a full distance matrix
dist_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to calculate the total and maximum distance of a tour
def evaluate_tour(tour):
    total_dist = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_dist = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_dist, max = dist

# Heuristic: Finding a good tour starting at the depot (greedy choice by nearest neighbour)
def find_tour():
    unvisited = list(range(1, len(cities)))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Get a tour using the heuristic
tour = find_tour()
total_travel_cost, max_distance = evaluate_tour(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)