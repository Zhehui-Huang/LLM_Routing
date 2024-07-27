import math
import random

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

def simulated_annealing(coordinates):
    current_temp = 1000
    cooling_rate = 0.995
    num_cities = len(coordinates)
    
    # Initial tour: simple sequential setup
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_tour.append(current_tour[0])  # ensure it's a round trip
    
    current_distance, current_max = calculate_total_distance(current_tour, coordinates)
    
    while current_temp > 1:
        # Pick two indices to swap (not the first city, which is the depot)
        i, j = random.sample(range(1, num_cities), 2)
        
        # Swap them to create a new candidate tour
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_tour[-1] = new_tour[0]  # ensure it remains a round trip
        
        # Calculate the new distance
        new_distance, new_max = calculate_total_distance(new_tour, coordinates)
        
        # Deciding if we should accept the new candidate
        if new_max < current_max or random.random() < math.exp((current_max - new_max) / current_temp):
            current_tour = new_tour
            current_distance = new_distance
            current_max = new_max
        
        # Cool down
        current_temp *= cooling_rate

    return current_tour, current_distance, current_max

# Coordinates of the cities including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

solution_tour, total_cost, max_consecutive_distance = simulated_annealing(coordinates)

print("Tour:", solution_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))