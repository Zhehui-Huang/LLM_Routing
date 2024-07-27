import itertools
import math

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cities coordinates including the depot
city_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

def find_optimal_tour():
    city_indices = list(range(1, 20))  # City indices excluding the depot
    shortest_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of 9 cities (as we include depot starting and ending, that totals 10 cities)
    for cities in itertools.combinations(city_indices, 9):
        # Create the tour starting and ending at depot city (0)
        tour = [0] + list(cities) + [0]
        
        # Calculate the total cost of the tour
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])

        # Check if this tour is better than the current best
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            best_tour = tour
            
    return best_tour, shortest_distance

# Get the best tour and calculate the corresponding distance
optimal_tour, optimal_distance = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_distance)