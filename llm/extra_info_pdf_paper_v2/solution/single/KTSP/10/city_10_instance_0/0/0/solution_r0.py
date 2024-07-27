import itertools
import math

# The coordinates for each city
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_tour():
    """ Find the shortest tour visiting exactly 4 cities including the depot city """
    min_cost = float('inf')
    best_tour = None
    
    # Consider combinations of 3 cities (excluding the depot city 0)
    for combination in itertools.combinations(range(1, 10), 3):
        # Create the tour starting and ending at city 0
        current_tour = [0] + list(combination) + [0]
        
        # Calculate the total travel cost of the current tour
        cost = sum(calculate_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        # Check if the current tour is better than what was found before
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour

    return best_tour, min_cost

# Calculate the optimal tour and its cost
optimal_tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)