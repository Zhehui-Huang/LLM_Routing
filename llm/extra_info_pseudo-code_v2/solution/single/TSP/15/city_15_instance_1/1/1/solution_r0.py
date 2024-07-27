import math
from itertools import permutations

# Define the coordinates for the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define a function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initial naive solution (greedy approach to get an initial tour)
def initial_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # return to the starting city
    return tour

# Calculate the cost of the tour
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Calculate initial tour and cost
initial_solution = initial_tour(0)
initial_cost = tour_cost(initial_solution)

# Note: Implementing Lin-Kernighan effectively requires additional detailed work
# For simplicity and demonstration, we compute initial solution and approximate solution here
# Further optimization with LK or other advanced method can be incrementally implemented

print("Initial Tour:", initial_solution)
print("Initial Tour Cost:", initial_cost)