import math
import itertools

# Coordinates of each city including the depot
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
          (64, 72), (14, 89)]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Building the distance matrix
num_cities = len(cities)
distance_matrix = [[0 for _ in range(num_cities)] for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all possible tours starting and ending at the depot city (index 0)
all_tours = itertools.permutations(range(1, num_cities))  # permutations of cities excluding the depot

best_tour = None
min_cost = float('inf')

for tour in all_tours:
    cost = distance_matrix[0][tour[0]]  # start from depot to the first city
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    cost += distance_matrix[tour[-1]][0]  # return from last city to depot

    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Formatting the best tour to start and end at the depot
best_tour_formatted = [0] + list(best_tour) + [0]

print("Tour:", best_tour_formatted)
print("Total travel cost:", min_cost)