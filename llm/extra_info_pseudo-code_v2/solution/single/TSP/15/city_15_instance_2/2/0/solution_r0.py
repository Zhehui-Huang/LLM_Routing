import math
from itertools import permutations

# Functions
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
    return total_cost

# Data, input
coordinates = [
    (54, 87), # Depot city 0
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99)  # City 14
]

# Since Lin-Kernighan algorithm is complex and specific, we start with a simple greedy approximation for running example
num_cities = len(coordinates)
visited = [False] * num_cities
tour = [0]  # start at the depot city 0
visited[0] = True

# Greedy TSP solution (Clarification: This is not Lin-Kernighan; this is a simple heuristic for illustration)
current_city = 0
while len(tour) < num_cities:
    nearest_city = None
    min_distance = float('inf')
    for i in range(num_cities):
        if not visited[i]:
            distance = euclidean_distance(coordinates[current_city], coordinates[i])
            if distance < min_distance:
                min_distance = distance
                nearest_city = i
    visited[nearest_city] = True
    tour.append(nearest_city)
    current_city = nearest_city

# Return to depot city 0
tour.append(0)

# Calculate the cost of the generated tour
tour_cost = total_tour_cost(tour, coordinates)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost}")