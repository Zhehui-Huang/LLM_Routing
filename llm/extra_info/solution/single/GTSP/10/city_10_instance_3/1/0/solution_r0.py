import itertools
import math

# Coordinates of cities
cities = {
    0: (84, 67),  # depot
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible tours that select one city from each group
def generate_possible_tours():
    # Generate all combinations of one city from each group
    product_of_groups = list(itertools.product(*city_groups))
    
    # Create full tours by returning to the depot
    for group_combination in product_of_groups:
        yield [0] + list(group_combination) + [0]

# Calculate the total cost of a tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Find the tour with the minimum cost
def find_optimal_tour():
    min_cost = float('inf')
    optimal_tour = []
    
    for tour in generate_possible_tours():
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            optimal_tour = tour
    
    return optimal_tour, min_cost

# Calculate the optimal tour and its cost
optimal_tour, total_cost = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)