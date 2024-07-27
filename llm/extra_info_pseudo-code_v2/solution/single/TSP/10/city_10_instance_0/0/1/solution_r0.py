import math
import itertools

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generates all permutations of cities (excluding the depot)
def generate_permutations():
    city_indices = list(cities.keys())
    city_indices.remove(0)  # Remove the depot
    return itertools.permutations(city_indices)

# Finding the shortest tour
def find_shortest_tour():
    shortest_tour = None
    min_cost = float('inf')

    for permutation in generate_permutations():
        # Calculate the cost of visiting the cities in this order, starting and ending at the depot
        current_tour = [0] + list(permutation) + [0]
        current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))

        # Update the shortest tour found so far
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour

    return shortest_tour, min_cost

# Use the function to find the shortest tour
tour, total_cost = find_shortest_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")