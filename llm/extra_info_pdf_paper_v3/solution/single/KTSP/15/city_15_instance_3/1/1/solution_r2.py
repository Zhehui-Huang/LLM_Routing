import math
import random

# Define the coordinates for each city including the depot
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to calculate the total tour distance
def calculate_tour_distance(tour, city_coords):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return distance

# Multi-start heuristic implementation
def multi_start_heuristic(k, iterations=100):
    best_tour = None
    best_cost = float('inf')
    all_cities = list(cities.keys())
    
    for _ in range(iterations):
        # Randomly select k-1 cities plus the depot
        selected_cities = random.sample(set(all_cities) - {0}, k-1)
        selected_cities = [0] + selected_cities + [0]  # start and end at depot
        
        # Iterate to find a better order by permuting the selected cities
        current_tour = selected_cities[:]
        random.shuffle(current_tour[1:-1])  # shuffle only the inner cities
        current_cost = calculate_tour_distance(current_tour, cities)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour

    return best_tour, best_cost

# Determine best route for the robot with given constraints
best_tour, best_cost = multi_start_heuristic(10)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)