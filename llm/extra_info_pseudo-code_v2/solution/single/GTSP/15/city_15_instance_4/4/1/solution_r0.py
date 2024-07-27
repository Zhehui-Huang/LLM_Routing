import math
import random

# Define the coordinates of the depot and the cities
coordinates = [
    (35, 40), # Depot City 0
    (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47),
    (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def random_tour():
    """Create a random tour starting from the depot, visiting one city from each group, and returning to the depot."""
    tour = [0]  # Start at depot
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # Return to depot
    return tour

# Initialize the best tour by generating a random tour
best_tour = random_tour()
best_cost = calculate_total_tour_cost(best_tour)

# Basic implementation of GLNS
num_trials = 100
for _ in range(num_trials):
    current_tour = random_tour()
    current_cost = calculate_total_tour_tree_cost(current_tour)
    if current_cost < best_cost:
        best_tour = current_tour
        best_cost = current_cost

# Output result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)