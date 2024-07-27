import math

# Constants and data given
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14,
    8, 7, 14, 19, 11, 26, 17, 6, 15
]

robot_capacities = [160, 160]
tours = [
    [0, 1, 3, 5, 7, 9, 11, 13, 16, 18, 15, 0],
    [0, 2, 4, 6, 8, 10, 12, 14, 17, 0]
]

travel_costs = [294.04, 193.13]
overall_cost = 487.17

def calculate_euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    # Check for correct starting and ending at the depot for each robot's tour
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check capacities not exceeded
    for i, tour in enumerate(tours):
        total_demand = sum(demands[city] for city in tour if city != 0)
        if total_demand > robot_capacities[i]:
            return "FAIL"
    
    # Check if each city is visited exactly once and its demand met
    all_cities_visited = set(city for tour in tours for city in tour if city != 0)
    if sorted(all_cities_visited) != list(range(1, len(coordinates))):
        return "FAIL"
    
    # Check calculated distances against the provided costs
    total_calculated_cost = 0
    for tour, expected_cost in zip(tours, travel_costs):
        calculated_cost = sum(calculate_euclidean_distance(tour[idx], tour[idx + 1]) for idx in range(len(tour) - 1))
        if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-2):
            return "FAIL"
        total_calculated_cost += calculated_cost
    
    if not math.isclose(total_calculated_cost, overall_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Running the verification
result = verify_SETUP_COMPLETE()
print(result)