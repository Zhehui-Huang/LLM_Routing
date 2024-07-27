import math
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}


# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)


# Generate all possible tours using a simple exhaustive search
def find_optimal_tour():
    city_list = list(cities.keys())
    city_list.remove(0)  # Exclude the depot initially for permutations
    shortest_tour = None
    min_cost = float('inf')

    # Generate permutations of cities (excluding depot)
    for permutation in permutations(city_list):
        # Calculate total distance including return to depot
        current_cost = 0
        prev_city = 0  # Start at the depot
        for city in permutation:
            current_cost += distance(prev_city, city)
            prev_city = city
        current_cost += distance(prev_city, 0)  # Return to the depot

        # Update optimal result
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = [0] + list(permutation) + [0]

    return shortest_tour, min_cost


# Calculate the optimal tour
optimal_tour, total_cost = find_optimal_tour()

# Prepare output as specified
output_tour = f"Tour: {optimal_tour}"
output_cost = f"Total travel cost: {total_cost}"

# Print the outputs
print(output_tour)
print(output_cost)