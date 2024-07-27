import itertools
import math

# Define city coordinates
cities = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Define groups of cities
city_groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(i, j):
    """ Calculate Euclidean distance between two points given their indices in the 'cities' list. """
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

def evaluate_tour(tour):
    """ Calculate the total distance of the tour. """
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(tour[i], tour[i+1])
    return total_dist

def find_best_tour():
    """ Finds the shortest possible tour visiting one city from each group and returning to the depot. """
    best_distance = float('inf')
    best_tour = None
    
    # Iterate over all possible combinations of cities, taking one city from each group
    for cities_combination in itertools.product(*city_groups):
        # Construct the tour starting and ending at depot
        tour = [0] + list(cities_combination) + [0]
        # Calculate this tour's total distance
        distance = evaluate_tour(tour)
        # Checking if newly calculated tour is better
        if distance < best_distance:
            best_distance = distance
            best_tour = tour
    
    return best_tour, best_distance

# Find and print the best tour
best_tour, best_distance = find_best_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance:.2f}")