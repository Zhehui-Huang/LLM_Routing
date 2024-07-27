import itertools

# City groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Function to calculate total tour distance given a list of city indices
def calculate_tour_distance(tour):
    total_distance = distance_matrix[tour[-1], tour[0]]
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i], tour[i+1]]
    return total_distance

# Generate all possible combinations of cities, taking exactly one city from each group
all_possible_tours = itertools.product(city_groups[0], city_groups[1], city_groups[2], city_groups[3])

# Append the depot city at the start and end of each tour
all_possible_tours = [[0] + list(tour) + [0] for tour in all_possible_tours]

# Find the tour with the minimum distance
min_tour = None
min_distance = float('inf')

for tour in all_possible_tours:
    current_distance = calculate_tour_distance(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        min_tour = tour

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance}")