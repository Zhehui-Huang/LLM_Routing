import math

# Given city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89),
}

# Calculate Euclidean Distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)

# Basic heuristic function to get a relatively short tour
def initial_tour():
    # Start at the depot, visit each city in increasing order (except depot, which is revisited at end)
    tour = list(range(n)) + [0]
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return tour, total_cost

# Simple heuristic to attempt to improve the tour (not truly Lin-Kernighan, but inspired swapping mechanism)
def optimized_tour(tour, total_cost):
    made_improvement = True
    best_tour = tour[:]
    best_cost = total_cost
    
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                # Try to swap two edges and see if it improves the cost
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1])
                new_cost = sum(distance_matrix[new_tour[i]][new_tour[i + 1]] for i in range(len(new_tour) - 1))
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    made_improvement = True
    
        tour = best_tour[:]
        total_cost = best_cost
    
    return best_tour, best_cost

# Start solving the problem
initial_tour, initial_cost = initial_tour()
optimized_tour, optimized_cost = optimized_tour(initial_tour, initial_cost)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost}")