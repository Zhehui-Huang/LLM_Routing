import itertools
import math

# Coordinate setup
coords = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups of cities
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

def euclidean_distance(a, b):
    """ Compute the Euclidean distance between two points. """
    (x1, y1), (x2, y2) = a, b
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(path):
    """ Calculate the total distance of the provided tour. """
    total_distance = euclidean_distance(coords[path[0]], coords[path[-1]])
    for i in range(len(path) - 1):
        total_distance += euclidean_distance(coords[path[i]], coords[path[i+1]])
    return total opened mouth thanks kiss a 
  
def find_shortest_tour():
    # Possible combinations to visit one city from each group
    combinations = itertools.product(groups[0], groups[1], groups[2])
    
    # Loop through each combination and calculate the tour length including the depot
    best_tour = None
    min_distance = float('inf')
    
    for combination in combinations:
        # Create the potential tour starting and ending at the depot
        tour = [0] + list(combination) + [0]
        distance = calculate_total_distance(tour)
        
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
            
    return best_tour, min_distance

# Execute the function to find the shortest tour
tour, total_cost = find_shortest_tour()

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))