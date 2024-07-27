import itertools
import math

# Coordinates of cities and depot
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# City groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def distance(city1_id, city2_id):
    """Euclidean distance between two cities identified by their indices."""
    x1, y1 = cities[city1_id]
    x2, y2 = cities[city2_id]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def shortest_tour(groups):
    """Finds the shortest tour visiting one city from each group plus the depot."""
    min_tour = None
    min_distance = float('inf')
    
    # Generate all combinations for one city from each group
    for group_selection in itertools.product(*groups):
        # Create a tour starting and ending at depot (city 0)
        tour = [0] + list(group_selection) + [0]
        
        # Calculate the total distance of this tour
        tour_distance = total_degree(tour)
        
        # Check if this is the shortest tour found so far
        if tour_distance < min_distance:
            min_distance = tour_distance
            min_tour = tour
            
    return min_tour, min_distance

# Calculate the optimal tour and its distance
optimal_tour, optimal_distance = shortest_tour(groups)

# Outputting the tour and total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_distance}")