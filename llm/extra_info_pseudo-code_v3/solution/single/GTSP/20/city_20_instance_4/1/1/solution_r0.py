from itertools import permutations
import math

# Define the city coordinates
cities = [
    (26, 60),  # Depot city (City 0)
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Define city groups
city_groups = [
    [5, 6, 16], 
    [8, 18, 19], 
    [11, 12, 13], 
    [1, 3, 9], 
    [2, 4, 14], 
    [10, 17], 
    [7, 15]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour):
    """Calculate the total tour cost given a tour of city indices."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Generate all possible tours by taking one city from each group
all_possible_tours = permutations([group[0] for group in city_groups])

# Find the shortest possible tour
shortest_tour = None
min_cost = float('inf')

for tour in all_possible_tours:
    current_tour = [0] + list(tour) + [0]
    cost = total_tour_cost(current_tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = current_tour

# Output the best tour and its total travel cost
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_cost:.2f}")