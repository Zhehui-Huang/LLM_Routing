import math
from itertools import permutations

# Define coordinates of the cities
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial tour generation using a heuristic (nearest neighbour)
def initial_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_other_city
    tour.append(start_city)  # Return to the start city
    return tour

# The 2-opt optimization algorithm
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i - 1], tour[i]) + distance(tour[j], tour[j + 1]) > \
                distance(tour[i - 1], tour[j]) + distance(tour[i], tour[j + 1]):
                    tour[i:j + 1] = tour[i:j + 1][::-1]  # Reverse the tour segment
                    improved = True
    return tour

# Compute the total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Execute the TSP solving process
initial = initial_tour(0)
optimized_tour = two_opt(initial)
total_cost = tour_cost(optimized_tour)

# Print results
output_tour = "Tour: " + str(optimized_tour)
output_cost = "Total travel cost: " + str(total_cost)

print(output_tour)
print(output_cost)