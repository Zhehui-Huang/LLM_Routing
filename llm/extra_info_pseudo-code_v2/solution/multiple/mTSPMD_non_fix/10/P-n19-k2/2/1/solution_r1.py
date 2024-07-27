import numpy as np
from math import sqrt

# City coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize random tours and calculate their cost
def initialize_tour():
    nodes = list(range(1, len(cities)))  # Exclude the starting depot
    np.random.shuffle(nodes)
    mid_index = len(nodes) // 2
    tour1 = [0] + nodes[:mid_index]
    tour2 = [0] + nodes[mid_index:]
    return tour1, tour2

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(tour[i - 1], tour[i])
    return total_cost

# Create two tours
tour1, tour2 = initialize_tour()

# Calculate tour costs
tour1_cost = calculate_tour_cost(tour1)
tour2_cost = calculate_tour_cost(tour2)
overall_cost = tour1_cost + tour2_cost

# Printing the results
print("Robot 0 Tour: [{}]".format(', '.join(map(str, tour1))))
print("Robot 0 Total Travel Cost:", tour1_cost)
print("\nRobot 1 Tour: [{}]".format(', '.join(map(str, tour2))))
print("Robot 1 Total Travel Cost:", tour2_cost)
print("\nOverall Total Travel Cost:", overall_cost)