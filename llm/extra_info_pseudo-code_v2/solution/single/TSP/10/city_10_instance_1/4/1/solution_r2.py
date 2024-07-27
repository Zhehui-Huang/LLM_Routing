import math
import itertools

# Define the coordinates of each city
cities = {
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

# A function to calculate the Euclidean distance between two points
def calculate_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Generate all permutations of the city indices except the depot city
city_indices = list(cities.keys())[1:]
permutations = itertools.permutations(city_indices)

# Function to calculate total cost of a tour
def total_cost(tour):
    cost = calculate_distance(cities[0], cities[tour[0]])  # from depot to first city
    for i in range(1, len(tour)):
        cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    cost += calculate_distance(cities[tour[-1]], cities[0])  # from last city to depot
    return cost

# Finding minimum cost tour
min_cost = float('inf')
best_tour = None

for perm in permutations:
    cost = total_cost(perm)
    if cost < min_cost:
        min_cost = cost
        best_tour = perm

# Constructing the complete tour starting and ending at the depot
final_tour = [0] + list(best_tour) + [0]

# Displaying the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")