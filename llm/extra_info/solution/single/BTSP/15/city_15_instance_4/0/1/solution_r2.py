import math
from itertools import permutations

# Define the coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate the Euclidean distance between two points.
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Find the optimal tour to minimize the longest distance between any two consecutive cities
def find_optimal_tour():
    # Initial values for comparisons
    min_max_distance = float('inf')
    optimal_tour = None
    
    # Generate all permutations of cities excluding the depot city
    base_cities = list(range(1, len(cities)))  # Exclude city 0 which is the depot
    all_tours = permutations(base_cities)
    
    for perm in all_tours:
        # Create a tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        
        # Calculate the total cost and the maximum distance in this tour
        total_cost = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        # Update the optimal tour if the max distance for this tour is smaller
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour
            min_total_cost = total_push_area_cost

    return optimal_tour, min_total_cost, min_max_distance

# Run the optimization function
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Print results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))