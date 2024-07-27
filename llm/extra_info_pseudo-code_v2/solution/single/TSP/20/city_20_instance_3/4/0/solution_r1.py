import math
import random

# Defining coordinates of the cities including the depot.
cities_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), 
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), 
    (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def simulated_annealing(cities):
    # Initial setup: start from the depot, visit all other cities once, and return to the depot
    current_tour = list(range(len(cities)))  # Start with a simple sequential tour
    current_tour.append(0)  # Make it a round trip
    current_distance = calculate_total_distance(current_tour, cities)
    
    temperature = 100.0
    alpha = 0.99
    min_temperature = 0.01
    
    while temperature > min_temperature:
        # Create new neighbor tour by swapping two cities
        new_tour = current_tour[:]
        l = random.randint(1, len(cities) - 2)
        r = random.randint(1, len(cities) - 2)
        new_tour[l], new_tour[r] = new_tour[r], new_tour[l]
        
        new_distance = calculate_total_distance(new_tour, cities)
        # Decide if the new tour should be accepted
        if (new_distance < current_distance or
            random.random() < math.exp((current_distance - new_distance) / temperature)):
            current_tour = new_tour
            current_distance = new_distance
        
        temperature *= alpha
    
    return current_tour, current_distance

# Run the simulated annealing algorithm
best_tour, best_distance = simulated_annealing(cities_coordinates)

print("Tour:", best_tour)
print("Total travel cost:", best_distance)