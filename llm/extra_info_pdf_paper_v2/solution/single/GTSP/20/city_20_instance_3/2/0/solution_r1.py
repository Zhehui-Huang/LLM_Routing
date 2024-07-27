import itertools
import math

# Define cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Define city groups
city_groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Selecting the nearest city in each group to the depot
chosen_cities = [min(group, key=lambda city: euclidean_distance(0, city)) for group in city_groups.values()]

# Define a function to calculate the total cost of a given tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to determine the best tour by iterating over permutations of chosen cities
def find_best_path(start, cities):
    # Initialize to a high value
    min_cost = float('inf')
    best_path = []
    # Check all permutations of the chosen cities
    for perm in itertools.permutations(cities):
        # Create a tour by starting and ending at the depot
        current_path = [start] + list(perm) + [start]
        # Calculate the cost of the current tour
        current_cost = calculate_tour_cost(current_path)
        # Update minimum cost and best path if a new minimum is found
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
    return best_path, min_cost

# Using the find_best_path function to find the optimal tour and its cost
best_tour, min_cost = find_best_path(0, chosen_cities)

# Output the tour and the total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")