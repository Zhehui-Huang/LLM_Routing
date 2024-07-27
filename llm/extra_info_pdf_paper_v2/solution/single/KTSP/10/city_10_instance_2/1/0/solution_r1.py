from itertools import permutations, combinations
import math

# City coordinates
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

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the shortest tour that includes exactly 6 cities
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Generate all combinations of 5 cities, excluding depot (0 is always included)
    for cities_subset in combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5):
        current_cities = [0] + list(cities_subset)
        
        # Generate permutations of the current subset of cities plus the depot
        for perm_city in permutations(current_cities):
            # Create a tour by going back to the depot
            tour = list(perm_city) + [0]
            
            # Calculate the total cost of this tour
            tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            
            # Check if this is the shortest tour found so far
            if tour_cost < min_cost:
                min_cost = tour_cost
                best_tour = tour
    
    return best_tour, min_cost

# Execute the function and output the results
best_tour, min_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")