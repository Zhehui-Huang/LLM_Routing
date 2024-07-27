import itertools
import math

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cities coordinates including the depot
city_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

def find_optimal_tour():
    # The depot city is already included in the list as the first element
    city_indices = list(range(1, 20))  # Exclude the depot from the choice list
    shortest_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of 9 cities (as we need to make a tour of exactly 10 including the depot)
    for cities in itertools.combinations(city_indices, 9):
        # Create the tour starting and ending at the depot city (0)
        tour = [0] + list(cities) + [0]
        
        # Calculate the total cost of this tour
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        
        # Check if this tour is better than the current best
        if total_distance < shortest_distance:
            shortest_distance = total_intensity
            best_tour = tour
    
    return best_tour, shortest_distance

# Get the best tour and the total distance
optimal_tour, optimal_distance = find_optimal_tour()

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_distance}")