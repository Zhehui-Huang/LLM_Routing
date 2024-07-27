import random
import math
from itertools import permutations

# Define the coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Helper function to calculate euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the total tour distance
def calculate_total_distance(tour):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return distance

def find_shortest_tour():
    # Setting a seed for reproducibility
    random.seed(0)

    # Selecting 15 different cities besides the depot (city 0)
    selected_cities = random.sample(range(1, 20), 15)
    selected_cities = [0] + selected_cities + [0]  # Adding the depot as start and end

    # Generate all possible permutations of the selected cities
    best_distance = float('inf')
    best_tour = None
    for perm in permutations(selected_cities[1:-1]):
        # Create a tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        distance = calculate_total_distance(tour)
        if distance < best_distance:
            best_distance = distance
            best_tour = tour

    return best_tour, best_distance

# Retrieve the optimal tour and its cost
best_tour, best_distance = find_shortest_tour()

# Print the output
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))