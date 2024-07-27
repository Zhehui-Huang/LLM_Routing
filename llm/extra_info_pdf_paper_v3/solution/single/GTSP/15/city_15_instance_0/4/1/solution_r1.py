import itertools
import math

# Coordinates of all cities including depot
coordinates = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39),
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12],
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_minimum_tour():
    """ Finds the minimal tour that visits one city from each group starting and ending at the depot """
    all_combinations = itertools.product(groups[0], groups[1], groups[2])
    min_distance = float('inf')
    best_tour = None
    
    for comb in all_combinations:
        # Each combination, along with the depot
        tour = [0] + list(comb) + [0]
        
        # Calculate the total distance for this tour
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += euclidean_distance(tour[i], tour[i+1])
        
        # Update minimum distance found
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour
    
    return best_tour, min_distance

# Compute the optimum tour and travel cost
optimal_tour, total_travel_cost = find_minimum_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_travel|;