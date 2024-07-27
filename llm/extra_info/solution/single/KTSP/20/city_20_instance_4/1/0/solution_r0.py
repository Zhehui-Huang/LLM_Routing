import math
from itertools import combinations, permutations

# Initialize cities' coordinates (city index corresponds to position)
coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
               (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
               (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_tour_cost(tour, coordinates):
    """Calculate the total distance of a given tour."""
    total_distance = 0.0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

# Let's proceed to find the tour
min_distance = float('inf')
best_tour = None

# Generate combinations of 15 cities (excluding the depot city at 0)
city_indices = list(range(1, 20))  # Cities excluding the depot
for cities in combinations(city_indices, 15):
    selected_cities = [0] + list(cities) + [0]  # includes depot at start and end
    
    # Generate possible permutations of the selected cities (the first and last cities are fixed)
    for perm in permutations(selected_cities[1:-1]):
        tour = [0] + list(perm) + [0]
        tour_distance = calculate_tour_cost(tour, coordinates)
        
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Output the best tour and corresponding total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)