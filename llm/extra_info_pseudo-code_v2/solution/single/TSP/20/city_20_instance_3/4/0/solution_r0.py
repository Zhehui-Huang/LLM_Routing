import math
import random

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour, cities):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

def simulated_annealing(cities):
    current_tour = list(range(len(cities)))
    current_tour.append(0)  # Returning to the depot city
    current_distance = calculate_total_distance(current_tour, cities)
    
    temperature = 100.0
    alpha = 0.99
    min_temperature = 1e-10
    while temperature > min_temperature:
        new_tour = current_tour[:]
        # Swap two cities in the tour (excluding the depot city 0 twice)
        left = random.randint(1, len(cities) - 2)
        right = random.randint(1, len(cities) - 2)
        new_tour[left], new_tour[right] = new_tour[right], new_tour[left]
        
        new_distance = calculate_total_distance(new_tour, cities)
        if new_distance < current_distance or random.uniform(0, 1) < math.exp((current_distance - new_distance) / temperature):
            current_tour, current_json = new_t: