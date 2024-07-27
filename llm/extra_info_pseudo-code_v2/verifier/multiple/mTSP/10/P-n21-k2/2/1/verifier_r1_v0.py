import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2)

def verify_solution(tours, costs, city_coordinates):
    city_visit_tracker = [0] * len(city_coordinates)
    computed_costs = []

    # Verify tours and compute costs
    for i, tour in enumerate(tours):
        # Check if tour starts and ends at the depot (city 0)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Compute the cost of the tour
        tour_cost = 0
        for j in range(len(tour)-1):
            x1, y1 = city_coordinates[tour[j]]
            x2, y2 = city_coordinates[tour[j+1]]
            distance = calculate_euclidean_distance(x1, y1, x2, y2)
            tour_cost += distance
            
            # Mark the city as visited
            city_visit_tracker[tour[j+1]] += 1

        computed_costs.append(round(tour_cost, 2))

        # Verify travel costs within marginal error
        if not math.isclose(tour_cost, costs[i], abs_tol=0.1):
            return "FAIL"

    # Verify all cities are visited exactly once, excluding the depot
    if any(visit != 1 for visit in city_visit_tracker[1:]):
        return "FAIL"

    # Verify overall cost
    if not math.isclose(sum(computed_costs), sum(costs), abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
                    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
                    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
                    (62, 63), (63, 69), (45, 35)]

tours = [
    [0, 12, 3, 18, 2, 7, 16, 5, 13, 19, 11, 0],
    [0, 8, 15, 10, 4, 1, 9, 17, 14, 20, 6, 0]
]

costs = [213.04, 168.72]

# Run verification
result = verify_solution(tours, costs, city_coordinates)
print(result)