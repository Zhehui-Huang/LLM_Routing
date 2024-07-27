import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (26, 60),   # depot
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Define city groups
city_groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Define the function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours by considering one city from each group
def generate_tours():
    for selection in permutations([min(group) for group in city_groups]):
        yield [0] + list(selection) + [0]

# Find the shortest tour
def find_shortest_tour():
    shortest_tour = None
    minimal_cost = float('inf')
    
    for tour in generate_tours():
        current_tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if current_tour_cost < minimal_cost:
            minimal_cost = current_tour_cost
            shortest_tour = tour
    
    return shortest_tour, minimal_cost

# Call the function to find the shortest tour
selected_tour, total_cost = find_shortest_tour()

# Output the results
print(f"Tour: {selected_tour}")
print(f"Total travel cost: {total_cost}")