import math

# City coordinates
cities = {
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

# Grouping of cities
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Function to compute the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Determine the shortest path visiting one city from each group
def find_optimal_path():
    min_total_distance = float('inf')  # Start with a very large number
    best_tour = []
    
    # Generate all combinations of visiting one city from each group (cartesian product of groups)
    from itertools import product
    for combination in product(*[groups[i] for i in range(3)]):
        # Generate a sequence of cities to visit starting and ending at depot city 0
        tour = [0] + list(combination) + [0]
        
        # Calculate the total distance of this tour
        total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Check if this tour is better than what we found before
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_tour = tour
    
    return best_tailed, total_distancence

# Use the function to find the optimal path and distance
optimal_tour, optimal_distance = find_optimal_path()

optimal_tour, optimal_distance