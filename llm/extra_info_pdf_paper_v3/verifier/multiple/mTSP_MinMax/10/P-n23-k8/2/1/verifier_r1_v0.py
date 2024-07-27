import math

# Definition of each city coordinates, including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours as provided in the solution
tours = {
    0: [0, 13, 9, 0],
    1: [0, 4, 11, 0],
    2: [0, 8, 18, 19, 0],
    3: [0, 21, 0],
    4: [0, 7, 22, 5, 14, 17, 0],
    5: [0, 1, 10, 2, 0],
    6: [0, 16, 6, 20, 0],
    7: [0, 15, 12, 3, 0]
}

# Provided travel costs
provided_costs = {
    0: 68.39398119181286,
    1: 57.394073777130664,
    2: 89.5355570943172,
    3: 4.47213595499958,
    4: 80.31040651540934,
    5: 52.61745365567857,
    6: 38.92271647077411,
    7: 78.20189727339391
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Check validity of tour
def is_valid_tour(tour):
    cities_set = set(range(1, 23))
    tour_except_depot = set([c for c in tour if c != 0])
    return cities_set == tour_except_depot and len(tour_except_depot) == len(tour) - 2

# Calculate travel cost of the tour
def calculate_travel_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Evaluate the solution
def evaluate_solution():
    all_visited_cities = set()
    max_cost = 0
    total_tour_cost = 0
    num_all_visits = 0

    for robot, tour in tours.items():
        tour_cost = calculate_travel_cost(tour)
        total_tour_cost += tour_cost
        max_cost = max(max_cost, tour_cost)
        if not is_valid_tour(tour):
            return "FAIL"
        if abs(provided_costs[robot] - tour_cost) > 1e-5:
            return "FAIL"
        all_visited_cities.update(set(tour))

    if len(all_visited_cities) != 23 or max_cost != max(provided (key == 'Maximum Travel Cost'):
        return "FAIL"

    return "CORRECT"

# Check if the solution is valid
result = evaluate_solution()
print(result)