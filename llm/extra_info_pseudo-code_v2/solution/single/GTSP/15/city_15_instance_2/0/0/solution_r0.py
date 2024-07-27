import math
import itertools

# Define the city coordinates, where the index corresponds to city number
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Define city groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(city_a, city_b):
    """ Calculate Euclidean distance between two cities based on their coordinates. """
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of a tour """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours considering one city from each group, starting and ending at the depot
def generate_tours():
    all_combinations = itertools.product(*city_groups)
    return [[0] + list(combination) + [0] for combination in all_combinations]

# Find the shortest valid tour
def find_shortest_tour():
    possible_tours = generate_tours()
    shortest_tour = min(possible_tours, key=calculate_tour_cost)
    return shortest_tour, calculate_tour_cost(shortest_tour)

# Solve the problem
tour, total_cost = find_shortest_tour()

# Output the tour and the total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")