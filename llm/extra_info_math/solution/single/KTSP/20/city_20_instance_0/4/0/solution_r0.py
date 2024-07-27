from itertools import permutations, combinations
import math

# Define city coordinates with city index as key
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to find the shortest tour
def find_shortest_tour(cities):
    min_cost = float('inf')
    best_tour = []
    
    # Generate all combinations of 3 other cities (+1 the depot city already included)
    for combo in combinations(cities.keys() - {0}, 3):
        # Create a possible tour by adding the depot city
        tour_cities = [0] + list(combo)
        
        # Generate all permutations of the selected cities for tours starting and ending in the depot
        for perm in permutations(tour_cities):
            # Ensure the tour starts and ends at the depot
            curr_tour = list(perm) + [0]
            
            # Calculate the total cost of this tour
            cost = sum(distance(curr_tour[i], curr_tour[i+1]) for i in range(len(curr_tour) - 1))
            
            # Update the minimum cost and the best tour found
            if cost < min_cost:
                min_cost = cost
                best_tour = curr_tour

    return best_tour, min_cost

# Solving the problem using the function defined
best_tour, min_cost = find_shortest_tour(cities)

print('Tour:', best_tour)
print('Total travel cost:', round(min_cost, 2))