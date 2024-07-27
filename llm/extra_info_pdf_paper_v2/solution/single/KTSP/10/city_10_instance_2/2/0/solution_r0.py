import math
from itertools import combinations, permutations

# Define the positions of all cities
cities = {
    0: (90, 3), 
    1: (11, 17), 
    2: (7, 27), 
    3: (95, 81), 
    4: (41, 54), 
    5: (31, 35), 
    6: (23, 95), 
    7: (20, 56), 
    8: (49, 29), 
    9: (13, 17)
}

def calculate_distance(city1, city2):
    """ Calculates the Euclidean distance between two city coordinates. """
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def find_shortest_route():
    min_tour = None
    min_cost = float('inf')
    
    # Get all 5-city combinations from the possible cities (excluding depot which is always included)
    city_combinations = combinations([i for i in cities.keys() if i != 0], 5)
    
    for combo in city_combinations:
        # Each combination will be tested with depot city as start and end
        possible_tours = permutations(combo)
        
        for tour in possible_tours:
            # Compute the cost of the tour including the return to the depot
            current_cost = calculate_distance(0, tour[0])
            for i in range(len(tour) - 1):
                current_cost += calculate_distance(tour[i], tour[i+1])
            current_cost += calculate_distance(tour[-1], 0)
            
            # Track the minimum cost and corresponding tour
            if current_cost < min_cost:
                min_cost = current_cost
                min_tour = [0] + list(tour) + [0]
    
    return min_tour, min_cost

# Compute the tour and cost
tour, total_cost = find_shortest_route()

# Output the results
print("Tour:", tour)
print("Total travel cost:", int(total_cost))  # Cast the cost to int for a cleaner output if required