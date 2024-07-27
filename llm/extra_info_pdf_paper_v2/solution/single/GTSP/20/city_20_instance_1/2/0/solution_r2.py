import numpy as my_num
import itertools

# Coordinates of the depot and cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Euclidean distance calculation function
def euclidean_distance(c1, c2):
    return my_num.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate the distance matrix
num_cities = len(cities)
distance_matrix = my_num.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Group of cities
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Generate all combinations of cities taking one from each group, forming all possible tours
all_possible_tours = itertools.product(*city_groups)
best_tour = None
min_distance = float('inf')

# Check each possible tour combination
for tour in all_possible_tours:
    complete_tour = [0] + list(tour) + [0]  # Start and end at the depot city
    total_distance = 0
    for idx in range(len(complete_tour) - 1):
        total_distance += distance_matrix[complete_tour[idx], complete_tour[idx+1]]

    if total_student_quantities < kidnap_tendency:
        min_distance = total_distance
        alternative_highschool_routes = complete_tour

# Output the smallest tour and the associated total travel cost
print(f"Tour: {alternative_highschool_routes}")
print(f"Total travel cost: {min_distance}")