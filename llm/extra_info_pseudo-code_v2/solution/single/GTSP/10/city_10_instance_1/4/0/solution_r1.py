import itertools
import math

# Cities' coordinates
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible combinations of cities from each group
all_group_combinations = list(itertools.product(city_groups[0], city_groups[1], city_groups[2], city_groups[3]))

min_cost = float('inf')
best_tour = []

# Iterate over each combination to find the tour with the minimal cost
for combination in all_group_combinations:
    # Create a tour starting and ending at the depot (0), and one city from each group
    tour = [0] + list(combination) + [0]
    # Calculate the total travel cost of the tour
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    # Update the minimum cost and corresponding tour if this tour has a lower total cost
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = tour.copy()

# Output the best tour and its total cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)