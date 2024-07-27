import math
from itertools import product

# Coordinates of the cities
city_coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups defined
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour):
    """Calculate the total travel distance for a given tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

def find_shortest_tour():
    """Find the shortest tour that visits one city from each group and returns to the depot."""
    min_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of cities, choosing one from each group
    for cities in product(*city_groups):
        # Create the full tour back to the depot
        tour = [0] + list(cities) + [0]
        distance = calculate_total_distance(tour)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
            
    return best_tour, min_distance

# Execution of the function to get the shortest tour and distance
tour, total_distance = find_shortest_tour()

# Print the results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_distance:.2f}')