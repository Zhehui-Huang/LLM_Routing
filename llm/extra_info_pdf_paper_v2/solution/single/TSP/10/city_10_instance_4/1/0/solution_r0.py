import math
import itertools

# Coordinates of the cities (depot included)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate a matrix of all distances
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = euclidean_distance(i, j)

# A greedy algorithm to provide an initial feasible solution
def initial_tour(depot):
    unvisited = set(cities.keys())
    unvisited.remove(depot)
    tour = [depot]
    current = depot
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(depot) # return to depot
    return tour

# Calculate total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

# Applying initial greedy tour approximation
tour = initial_tour(0)
tour_cost = calculate_tour_cost(tour)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {tour]  COST).tour_cost:.2f}")

# This code produces an initial feasible solution. Further improvements can be added by implementing more advanced heuristic methods.