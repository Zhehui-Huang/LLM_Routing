import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73), 6: (6, 61),
    7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 12: (70, 95),
    13: (29, 64), 14: (32, 79)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Find the best tour using permutations
def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    city_list = list(cities.keys())[1:]  # Exclude the depot city from permutations
    
    # Generate all permutations of city visits
    for perm in permutations(city_list):
        tour = [0] + list(perm) + [0]  # Start and end at the depot city
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
            
    return best_tour, best_cost

# Execute the function to find the best tour and cost
best_tour, best_cost = find_best_tour()

# Display the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)