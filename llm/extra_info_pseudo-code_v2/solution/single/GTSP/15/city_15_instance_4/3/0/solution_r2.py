import random
import math

# Coordinates of cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate an initial tour by selecting a random city from each group
def generate_initial_tour():
    tour = [0]  # Start at the city depot (index 0)
    selected_cities = set([0])

    # Select one city from each group
    for group in groups:
        city = random.choice(group)
        while city in selected_cities:
            city = random.choice(group)
        tour.append(city)
        selected_cities.add(city)

    tour.append(0)  # Return to the city depot
    return tour

# Calculate the cost of a given tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Main function to determine the shortest tour
def determine_shortest_tour():
    best_tour = None
    lowest_cost = float('inf')

    # Try multiple initial tours to find the one with the lowest cost
    attempts = 1000
    for _ in range(attempts):
        initial_tour = generate_initial_tour()
        cost = tour_cost(initial_tour)

        if cost < lowest_cost:
            best_tour = initial_tour
            lowest_cost = cost

    return best_tour, lowest_cost

# Calculate the shortest tour and display the results
best_tour, best_cost = determine_shortest_tour()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)