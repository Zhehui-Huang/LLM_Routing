import math
from itertools import permutations

# Define the coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible tours
def generate_tours():
    base_cities = list(range(1, len(cities)))  # Excluding depot city
    for perm in permutations(base_cities):
        tour = [0] + list(perm) + [0]
        yield tour

# Find optimal tour minimizing the maximum distance between two consecutive cities
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    all_tours = generate_tours()
    
    for tour in all_tours:
        max_distance = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            total_cost += distance
            if distance > max_distance:
                max_distance = distance
        
        if max_distance < min_max_working_distance:
            min_max_distance = max_distance
            min_total_cost = total_cost
            optimal_tour = tour
            
    return optimal_tour, min_total_cost, min_max_distance

# Execute the function to get the desired output
optimal_tour, total_cost, max_distance = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))