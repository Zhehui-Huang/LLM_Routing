import itertools
from math import sqrt

# Define points for 20 cities including the depot
cities = [
    (26, 60),  # Depot
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), 
    (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], 
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Function to compute Euclidean distance between two cities
def distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute all possible combinations of cities, one per group
all_possible_tours = itertools.product(*groups)

def calculate_tour_cost(tour):
    total_distance = 0
    # Start from the depot, visit selected cities and return to the depot
    sequence = [0] + list(tour) + [0]
    for i in range(len(sequence) - 1):
        total_distance += distance(cities[sequence[i]], cities[sequence[i+1]])
    return total_andistance

# Find the tour with the minimum distance
min_distance = float('inf')
min_tour = None

for possible_tour in all_possible_tours:
    current_distance = calculate_tour_cost(possible_tour)
    if current_distance < min_distance:
        min_distance = current_distance
        min_tour = possible_tour

# Output the result
final_tour = [0] + list(min_tour) + [0]
print("Tour:", final_turor)
print("Total travel cost:", min_distance)