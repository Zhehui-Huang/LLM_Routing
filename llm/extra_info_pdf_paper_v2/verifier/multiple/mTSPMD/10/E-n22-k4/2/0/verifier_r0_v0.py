import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, costs, overall_cost):
    cities_visited = set()
    actual_costs_computed = []
    coordinates = [(145, 215), (151, 264), (159, 261), (130, 254),
                   (128, 252), (163, 247), (146, 241), (161, 242),
                   (142, 239), (163, 236), (148, 232), (128, 231),
                   (156, 217), (129, 214), (146, 208), (164, 208),
                   (141, 206), (147, 193), (164, 193), (129, 189),
                   (155, 185), (139, 182)]

    # Requirement 1: Check tours start and end at the assigned depots
    assigned_depots = [0, 1, 2, 3]
    for index, tour in enumerate(tours):
        if tour[0] != tour[-1] or tour[0] != assigned_depots[index]:
            return "FAIL: Tours must start and end at the assigned depots."

    # Requirement 2: Check that each city is visited exactly once
    for tour in tours:
        for city in tour[1:-1]:  # Exclude the depots at the ends
            if city in cities_visited:
                return "FAIL: Each city must be visited exactly once."
            cities_visited.add(city)
    if len(cities_visited) != 22 - 4:  # Exclude the depot cities from the total count
        return "FAIL: Some cities were not visited."

    # Calculate and compare travel costs
    total_calculated_cost = 0
    for index, tour in enumerate(tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        actual_costs_computed.append(round(tour_cost, 2))
        total_calculated_cost += tour_cost
        if not math.isclose(tour_cost, costs[index], abs_tol=0.1):
            return f"FAIL: Tour cost mismatch for robot {index}. Expected: {costs[index]}, Computed: {round(tour_cost, 2)}"

    # Requirement 3: Check total cost
    if not math.isclose(total_calculated_cost, overall_cost, abs_tol=0.1):
        return "FAIL: Overall cost does not match the expected value."

    return "CORRECT"

# Data from the provided solution
tours = [
    [0, 6, 13, 14, 21, 0],
    [1, 7, 10, 11, 18, 1],
    [2, 4, 5, 9, 12, 15, 16, 17, 20, 2],
    [3, 8, 19, 3]
]
costs = [145.75, 185.12, 235.75, 135.88]
overall_cost = 702.49

# Verification
result = verify_solution(tours, costs, overall_cost)
print(result)