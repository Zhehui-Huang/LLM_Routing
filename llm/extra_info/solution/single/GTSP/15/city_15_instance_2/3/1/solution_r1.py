import itertools
import math

# City coordinates
city_coords = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# City groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Generate all combinations of cities from each group
all_possible_tours = itertools.product(*city_groups)

best_tour = None
best_cost = float('inf')

# Iterate through all possible tours
for tour in all_possible_tours:
    # Construct the tour starting and ending at the depot (city 0)
    tour_with_depot = [0] + list(tour) + [0]
    
    # Compute the total travel cost of this route
    total_cost = sum(euclidean_distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot) - 1))
    
    # Check if the current tour has a lower cost than the best found so far
    if total_cost < best_cost:
        best_cost = total_cost
        best_tour = tour_with_depot

# Output the best tour and total cost
output_result = {
    'Tour': best_tour,
    'Total travel cost': best_cost
}

print("Tour:", output_result['Tour'])
print("Total travel cost:", round(output_result['Total travel cost'], 2))