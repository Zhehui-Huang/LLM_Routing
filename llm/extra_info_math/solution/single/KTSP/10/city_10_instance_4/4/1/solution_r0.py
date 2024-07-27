import math
from itertools import combinations

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Possible combinations of 7 cities excluding the depot
city_indices = list(cities.keys())[1:]  # excludes the depot initially
city_combinations = combinations(city_indices, 7)  # combinations of 7 cities

# Evaluate each combination by creating a circuit starting and ending at the depot (0)
best_tour = None
min_cost = float('inf')

for combination in city_combations:
    # Include the depot city in the current tour
    tour = [0] + list(combination)
    
    # Find the minimum tour cost using a greedy nearest-neighbour approach
    def find_min_tour(tour):
        current_city = tour[0]
        unvisited = set(tour[1:])
        path = [current_city]
        tour_cost = 0
        
        while unvisited:
            next_city = min(unvisited, key=lambda x: distance(current_city, x))
            tour_cost += distance(current_city, next_city)
            current_city = next_city
            path.append(current_city)
            unvisited.remove(current_city)
        
        # Return to the depot
        tour_cost += distance(current_city, 0)
        path.append(0)
        
        return tour_cost, path
    
    current_cost, current_tour = find_min_tour(tour)
    
    # Update the best tour found so far
    if current_cost < min_cost:
        best_tour = current_tour
        min_cost = current_cost

# Output the final best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")