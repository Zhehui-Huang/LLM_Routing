import math
import random

# Cities coordinates
coordinates = [
    (35, 40),  # Depot
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Grouping of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

def calculate_distance(c1, c2):
    # Using Euclidean distance
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_tour_cost(tour):
    # Calculate the total distance of a tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def initial_tour():
    # Create an initial tour by randomly picking one city from each group and return to the depot
    tour = [0]  # start at depot
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # return to depot
    return tour

def local_search(tour):
    # Simple local search to swap two cities and see if it improves the tour
    best_tour = tour[:]
    best_cost = total_tour_cost(tour)
    
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
            new_cost = total_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tours = new_tour[:]
                best_cost = new_cost

    return best_tour

# Performing a simplified version of the GLNS algorithm
def find_best_tour():
    best_tour = initial_tour()
    best_cost = total_tour_cost(best_tour)
    
    for _ in range(100):  # Number of trials
        current_tour = initial_tour()
        current_tour = local_search(current_tour)
        current_cost = total_tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost
            
    return best_tour, best_cost

# Find the best tour using the algorithm
best_tour, best_cost = find_best_tour()

# Output the solution
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))