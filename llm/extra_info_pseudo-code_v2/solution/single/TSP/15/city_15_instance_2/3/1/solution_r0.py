import math
from itertools import permutations

# Coordinates for each city
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    (x1, y1), (x2, y2) = coordinates[a], coordinates[b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of the entire tour."""
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def simplified_lin_kernighan():
    # Initial assumption: use a naive approach as the starting tour
    # Start at city 0, visit all cities in numeric order and then return to city 0
    n = len(coordinates)
    min_tour = list(range(n)) + [0]  # A tour that visits cities from 0 up to n-1 and returns to 0
    
    # Calculate the total tour cost
    min_cost = total_tour_cost(min_tour)
    
    # Use a simple tour optimization technique: try swapping pairs of cities
    # Note: This is a placeholder for an adapted algorithm, not the complete Lin-Kernighan Heuristic
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            new_tour = min_tour[:]
            # Swap two cities in the tour
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour)
            if new_cost < min_cost:
                min_tour, min_cost = new_tour, new_cost
            
    return min_tour, min_cost

# Computing the tour and cost
solution_tour, solution_cost = simplified_lin_kernighan()

# Output the result
print(f"Tour: {solution_tour}")
print(f"Total travel cost: {round(solution_cost, 2)}")