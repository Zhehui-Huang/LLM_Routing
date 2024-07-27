import itertools
import math

# Coordinates of the cities, including the depot (city 0)
cities = {
    0: (16, 90),  1: (43, 99),  2: (80, 21),  3: (86, 92),  4: (54, 93),  
    5: (34, 73),  6: (6, 61),   7: (86, 69),  8: (30, 50),  9: (35, 73),
    10: (42, 64), 11: (64, 30),  12: (70, 95), 13: (29, 64), 14: (32, 79)
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
    """Calculate the Euclidean distance between two cities identified by their indices."""
    x1, y1 = cities[city1_id]
    x2, y2 = cities[city2_id]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(tour):
    """Calculate the total distance of the given tour."""
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def shortest_tour(groups):
    """Determine the shortest tour that visits one city from each group and returns to the start."""
    min_tour = None
    min_distance = float('inf')
    
    # Generate all possible combinations for selecting one city from each group
    for group_selection in itertools.product(*groups):
        # Create a tour starting and ending at the depot city (index 0)
        tour = [0] + list(group_selection) + [0]
        
        # Calculate the distance of this tour
        current_distance = total_distance(tour)
        
        # Update the shortest found tour and its distance
        if current_distance < min_distance:
            min_distance = current_distance
            min_tour = tour
    
    return min_tour, min_distance

# Get the optimal tour and its total distance
optimal_tour, optimal_distance = shortest_tour(groups)

# Output the tour and total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_distance:.2f}")