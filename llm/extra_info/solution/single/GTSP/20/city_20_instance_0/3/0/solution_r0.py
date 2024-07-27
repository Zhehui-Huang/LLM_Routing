import math
from itertools import product

# Define the cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Group of cities - each list corresponds to a group
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x_dist = cities[city1][0] - cities[city2][0]
    y_dist = cities[city1][1] - cities[city2][1]
    return math.sqrt(x_dist**2 + y_dist**2)

# Finding the shortest tour
def find_shortest_tour(groups):
    min_dist = float('inf')
    best_tour = []
    
    # Generate all combinations of choosing one city from each group
    for comb in product(*groups):
        # Include the depot as the start and end point of the tour
        tour = [0] + list(comb) + [0]
        
        # Calculate the travel cost of this tour
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i+1])
        
        # Check if this is the shortest tour found so far
        if cost < min_dist:
            min_dist = cost
            best_tour = tour
    
    return best_tour, min_dist

# Execute the function
tour, total_cost = find_shortest_tour(groups)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")