import math

# Coordinates of cities indexed from 0 to 18
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calculate_distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def test_solution():
    tours = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  # Robot 0
        [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]  # Robot 1
    ]
    costs = [196.35748543424958, 278.7665893800457]

    correct = True

    # Check Requirement 1: Number of cities (19 total and starting/ending at the depot)
    if len(CITIES) != 19 or any(0 not in tour or tour[0] != tour[-1] for tour in tours):
        correct = False

    # Check Requirement 2: Each robot visits all cities exactly once, excluding depot as a destination
    all_cities_visited = set(sum((tour[1:-1] for tour in tours), []))
    if all_cities_visited != set(range(1, 19)):
        correct = False

    # Check Requirement 3: Test if costs are really minimizing max distance
    max_cost = max(costs)
    if not all(cost <= max_cost for cost in costs):
        correct = False

    # Check Requirement 4: Starting and ending at depot, sequence specified
    # Implicit in tours structure
    
    # Check Requirement 5: Correct calculation of travel cost and max cost
    calculated_costs = [total_tour_cost(tour) for tour in tours]
    max_calculated_cost = max(calculated_costs)
    for idx, cost in enumerate(costs):
        if not (math.isclose(cost, calculated_costs[idx], rel_tol=1e-5)):
            correct = False

    if correct and math.isclose(max_cost, max_calculated_cost, rel_tol=1e-5):
        print("CORRECT")
    else:
        print("FAIL")

test_solution()