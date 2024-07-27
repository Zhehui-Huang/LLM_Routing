import math
from itertools import permutations

# Coordinates of each city, including the depot (index 0)
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of cities
num_cities = len(cities)

# Calculate all distances between each pair of cities
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(i, j)

# Find the shortest path using a brute-force approach
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    cities_to_visit = list(range(1, num_cities))  # excluding the depot city 0
    
    for perm in permutations(cities_to_visit):
        current_cost = 0
        # Tour starts and ends at the depot city, 0
        current_tour = [0] + list(perm) + [0]
        
        # Calculate the cost of the current tour
        for k in range(len(current_tour) - 1):
            current_cost += distances[current_tour[k]][current_tour[k+1]]
        
        # Update minimum cost and best tour
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
            
    return best_tour, min_cost

# Execute the function to find the shortest tour
tour, total_cost = find_shortest_tour()

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)