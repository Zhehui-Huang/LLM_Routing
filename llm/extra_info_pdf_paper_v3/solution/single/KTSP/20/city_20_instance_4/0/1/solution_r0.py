import math
import random

# Coordinates of the cities
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate the total cost of a tour
def calculate_cost(tour):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += distance(tour[i], tour[i+1])
    return tour_cost

# Heuristic function to generate initial solution (simple nearest neighbor)
def nearest_neighbor(start_city, k):
    tour = [start_city]
    available_cities = list(range(1, 20))
    current_city = start_city

    while len(tour) < k:
        next_city = min(available_cities, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city

    tour.append(start_city) # return to the depot
    return tour

# Heuristic modification function (two-opt swap to optimize route)
def two_opt_swap(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # do not swap consecutive cities
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Main TSP function
def k_TSP():
    initial_tour = nearest_neighbor(0, 16)  # Start with the depot and select 16 cities
    optimized_tour = two_opt_swap(initial_tour)
    total_cost = calculate_cost(optimized_tour)
    
    return optimized_tour, total_cost

# Executing the TSP solver
final_tour, final_cost = k_TSP()

# Outputting the result
print("Tour:", final_tour)
print("Total travel cost:", final_cost)