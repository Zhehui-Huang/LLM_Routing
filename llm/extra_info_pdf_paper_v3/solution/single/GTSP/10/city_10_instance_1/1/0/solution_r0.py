import math
from itertools import product

# City coordinates: city index to (x, y)
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

def calculate_distance(city1, city2):
    """
    Calculate Euclidean distance between two cities.
    """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_shortest_tour():
    """
    Find the shortest tour that visits one city from each group starting and ending at the depot.
    """
    min_tour = None
    min_cost = float('inf')
    
    # Generate all combinations by selecting one city from each group
    for combination in product(*groups):
        # Create a potential tour beginning and ending at the depot (0)
        tour = [0] + list(combination) + [0]
        
        # Calculate the cost of this tour
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i+1])
        
        # Track the minimum cost and corresponding tour
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
            
    return min_tour, min_cost

# Execute the function to find the shortest tour and total travel cost
tour, total_cost = find_shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")