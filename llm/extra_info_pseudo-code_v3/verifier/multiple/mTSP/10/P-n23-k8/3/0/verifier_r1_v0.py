import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(robots_tours, city_coords):
    # Prepare city visit verification
    city_visit = set()
    total_calculated_cost = 0.0
    # Coordinates of cities
    coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }

    # Validate each robot's tour
    for tour_data in robots_tours:
        tour = tour_data['tour']
        reported_cost = tour_data['cost']
        # Tour should start and end at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Compute the cost of the tour and verify all cities are visited exactly once
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                city_visit.add(tour[i])
            x1, y1 = coords[tour[i]]
            x2, y2 = coords[tour[i + 1]]
            tour_cost += calculate_euclidean_distance(x1, y1, x2, y2)
        
        # Check calculated cost vs reported cost
        if not math.isclose(tour_cost, reported_cost, rel_tol=1e-2):
            return "FAIL"

        total_calculated_cost += tour_cost

    # All cities except the depot must be visited exactly once
    if len(city_visit) != 22:
        return "FAIL"

    overall_reported_cost = sum([x['cost'] for x in robots_tours])
    # Validate total cost
    if not math.isclose(total_calculated_cost, overall_reported_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Robot tours data as provided in the solution
robots_tours = [
    {"tour": [0, 22, 19, 0], "cost": 102.86},
    {"tour": [0, 21, 15, 0], "cost": 62.48},
    {"tour": [0, 6, 18, 0], "cost": 81.18},
    {"tour": [0, 2, 11, 0], "cost": 78.25},
    {"tour": [0, 1, 12, 0], "cost": 60.01},
    {"tour": [0, 13, 14, 0], "cost": 80.99},
    {"tour": [0, 17, 8, 0], "cost": 89.55},
    {"tour": [0, 16, 10, 4, 3, 7, 5, 20, 9, 0], "cost": 143.61}
]

# Call the verification function
result = verify_solution(robots_tours, city_coords={i: (30, 40) for i in range(23)})  # Dummy coords for cities
print(result)