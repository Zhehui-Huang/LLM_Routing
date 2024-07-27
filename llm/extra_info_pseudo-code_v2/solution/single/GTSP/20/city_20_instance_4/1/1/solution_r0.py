import math
import random

# Coordinates of the depot and cities
coordinates = [
    (26, 60), # Depot - City 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), 
    (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], 
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def initial_tour(groups):
    tour = [0]  # Start at the depot
    for group in groups:
        selected_city = random.choice(group)
        tour.append(selected_city)
    tour.append(0)  # Return to the depot
    return tour

def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

def find_best_tour(groups, iterations=10000):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(iterations):
        random_tour = initial_tour(groups)
        cost = tour_cost(random_tour)
        if cost < best_cost:
            best_tour = random_tour
            best_cost = cost
    
    return best_tour, best_cost

# Run the optimization
best_tour, best_cost = find_best_tour(groups)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))