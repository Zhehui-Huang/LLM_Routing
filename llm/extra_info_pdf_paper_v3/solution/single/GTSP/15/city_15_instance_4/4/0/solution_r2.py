import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# City groups as provided in the problem description
city_groups = [
    [3, 8],       # Group 0
    [4, 13],      # Group 1
    [1, 2],       # Group 2
    [6, 14],      # Group 3
    [5, 9],       # Group 4
    [7, 12],      # Group 5
    [10, 11]      # Group 6
]

def find_shortest_tour():
    # Generate all possible combinations of each city from each group
    all_combinations = list(itertools.product(*city_groups))

    # Include the depot city at the start and the end of the tour
    all_possible_tours = [[0] + list(combination) + [0] for combination in all_combinations]

    # Find tour with the minimum travel cost
    min_distance = float('inf')
    best_tour = None

    for tour in all_possible_tours:
        total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

    return best_tour, min_distance

# Get the best tour and its total distance
optimal_tour, total_travel_cost = find_shortest_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_travel_cost, 2))