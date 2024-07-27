def validate_solution(tours, costs, overall_cost):
    from math import sqrt

    def distance(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # City coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    unique_cities = set(range(1, 21))  # Exclude depot in check
    visited_cities = set()

    # Check each robot's tour
    tour_costs = []
    for tour, expected_cost in zip(tours, costs):
        # Ensure tour starts and ends at depot
        if not (tour[0] == 0 and tour[-1] == 0):
            return "FAIL"
        
        # Calculate actual cost of the tour
        path_cost = 0.0
        for i in range(len(tour) - 1):
            cost = distance(coordinates[tour[i]], coordinates[tour[i + 1]])
            path_cost += cost
            if tour[i] != 0:  # Exclude multiple checks for depot
                visited_cities.add(tour[i])
        
        if abs(path_cost - expected_cost) > 1e-6:  # Allow for floating-point error
            return "FAIL"
        
        tour_costs.append(path_cost)
    
    # Ensure all cities visited exactly once
    if unique_cities != visited_cities:
        return "FAIL"
    
    # Check the overall cost
    if abs(sum(tour_costs) - overall_cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Provided solution information
tours = [
    [0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16, 0, 0],
    [0, 1, 10, 4, 11, 15, 12, 3, 19, 18, 8, 2, 7, 13, 9, 17, 14, 5, 20, 6, 0, 0]
]
tour_costs = [200.0, 178.65082474133712]
overall_cost = 378.65082474133715

# Verify the solution is correct
result = validate_solution(tours, tour costs, overall_cost)
print(result)