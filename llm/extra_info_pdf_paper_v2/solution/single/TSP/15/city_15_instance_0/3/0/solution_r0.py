import math
from itertools import permutations

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Approximate a solution via a greedy nearest neighbor algorithm
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # return to the depot city
    return tour

# 2-opt Swap function
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Function to compute total distance of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Initial greedy tour
initial_tour = nearest_neighbor_tour(0)

# Optimized tour with 2-opt
optimized_tour = two_opt(initial_tour)

# Calculate the total travel cost of the optimized tour
total_cost = tour_cost(optimized_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")