import itertools
import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# City groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to find the minimum travel cost visiting one city from each group and returning to the depot
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []

    # Generate all permutations of one city per group
    city_permutations = list(itertools.product(*city_groups))

    # Try each permutation for the minimum cost tour
    for perm in city_permutations:
        current_tour = [0] + list(perm) + [0]
        current_cost = sum(calculate_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))

        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

    return best_tour, min_cost

# Call the function to find the shortest tour and total cost
tour, total_cost = find_shortest_tour()

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)