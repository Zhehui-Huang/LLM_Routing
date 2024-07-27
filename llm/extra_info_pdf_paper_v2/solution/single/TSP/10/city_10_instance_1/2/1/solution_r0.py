import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Calculate total distance of a given tour
def tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Function to find the shortest tour using permutations (brute force approach)
def find_shortest_tour():
    city_indices = list(cities.keys())
    city_indices.pop(0)  # Remove the depot city from the list to generate permutations
    all_tours = permutations(city_indices)
    shortest_tour = None
    min_distance = float('inf')
    
    for tour in all_tours:
        # Create a full tour starting and ending at the depot city
        current_tour = [0] + list(tour) + [0]
        current_distance = tour_distance(current_tour)
        
        # Update the best tour found
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour
    
    return shortest_tour, min_distance

# Get the solution
optimal_tour, optimal_distance = find_shortest_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_distance))