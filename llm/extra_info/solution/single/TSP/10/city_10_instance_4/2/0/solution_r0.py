import math
import itertools

# Coordinates of the cities
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Construction of distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = distance(i, j)

# Function to find the minimum cost using permutations (brute force approach for simplicity and clarity)
def find_tsp_tour():
    # Generate all possible tours from city 0 to all other cities and back to 0
    city_indices = list(range(1, n))  # Exclude the depot city for permutation
    all_tours = itertools.permutations(city_indices)
    min_cost = float('inf')
    best_tour = None
    
    for tour in all_tours:
        cost = distance_matrix[0][tour[0]] + distance_matrix[tour[-1]][0]  # Start and end at the depot
        cost += sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))  # Sum the cost of intermediate travel
        
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return [0] + list(best_tour) + [0], min_cost

# Get the best tour and the minimum cost
best_tour, min_cost = find_tsp_tour()

# Output result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)