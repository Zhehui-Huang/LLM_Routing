import math
from itertools import permutations

# Define cities coordinates indexed from 0 (depot) to 19
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_type(cities[i], cities[j])

def calculate_tour_cost(tour):
    """ Calculate the total cost of a tour based on the distance matrix. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost + distance_matrix[tour[-1]][tour[0]]  # returning to the depot

# Generate all possible tours starting and ending at the depot (city 0)
all_tours = permutations(range(1, num_cities))  # omitting the depot city (0)
shortest_tour = None
min_cost = float('inf')

for tour in all_tours:
    # create a full tour by adding the depot (0) at the start and end
    full_tour = [0] + list(tour) + [0]
    cost = calculate_tour_cost(full_tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = full_tour

# Output the shortest tour and the minimal cost
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)