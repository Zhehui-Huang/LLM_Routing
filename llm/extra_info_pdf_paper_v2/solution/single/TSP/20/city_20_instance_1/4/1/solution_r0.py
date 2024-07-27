import math
import random

# Define the city coordinates
city_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Calculate Euclidean distance between cities
def calc_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Generate an initial solution (greedy start)
def initial_tour():
    unvisited = list(range(1, len(city_coords)))  # start with city 0 as depot
    tour = [0]
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_id

    tour.append(0)  # return to the depot
    return tour

# Function to compute the total travel cost of the tour
def total_travel_cost(tour):
    total_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

# Perform heuristic improvements on the tour (e.g., 2-opt swaps)
def improve_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # Consecutive edges, no swap needed
                if calc_distance(tour[i], tour[j]) + calc_distance(tour[i-1], tour[j+1]) < calc_distance(tour[i], tour[i-1]) + calc_distance(tour[j], tour[j+1]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Compute the solution
initial_path = initial_tour()
improved_path = improve_tour(initial_path)
total_cost = total_travel_cost(improved_path)

# Output the solution
print("Tour:", improved_path)
print("Total travel cost:", total_cost)