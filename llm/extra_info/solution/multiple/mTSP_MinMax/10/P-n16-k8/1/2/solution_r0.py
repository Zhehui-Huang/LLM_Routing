import math
from itertools import permutations

# Define the city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of robots
num_robots = 8

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate the distance matrix
distance_matrix = [
    [euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(len(city_coordinates))]
    for i in range(len(city_coordinates))
]

# Function to calculate the total cost of a tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Helper function to find the complete tour cost from depot, visiting each city, and back to depot
def get_full_tour_cost(tour):
    complete_tour = [0] + tour + [0]
    return calculate_tour_cost(complete_tour)