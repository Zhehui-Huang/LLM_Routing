import math
import itertools

# Coordinates of the cities
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between two points
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generating distance matrix
distance_matrix = [[calc_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Number of cities to include in the tour including the depot
k = 10

# Function to search the best possible tour
def find_best_tour():
    min_cost = float('inf')
    best_tour = None

    # Combination of 9 other cities along with depot, minus 1 as depot is always in tour
    for combination in itertools.combinations(range(1, len(cities)), k - 1):
        current_combination = [0] + list(combination)  # Include depot city in current list

        # Calculate all permutations among the selected combination excluding the depot
        for permutation in itertools.permutations(current_combination[1:]):
            tour = [0] + list(permutation) + [0]  # Starting and ending at depot

            # Calculate cost of current permutation
            cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

            # Determine if current cost is less than the known minimum
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Obtain result
best_tour, min_cost = find_best_tour()

# Output solution
print("Tour:", best_tour)
print("Total travel cost:", min_cost)