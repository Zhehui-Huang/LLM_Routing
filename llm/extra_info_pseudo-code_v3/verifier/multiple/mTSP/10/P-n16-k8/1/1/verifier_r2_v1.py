import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, travel_costs, coordinates):
    depot = coordinates[0]
    num_cities = len(coordinates)
    visited_cities = set()

    overall_travel_cost_calculated = 0

    for i, tour in enumerate(tours):
        # Check tour start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate travel cost of the tour
        calculated_cost = 0
        for j in range(len(tour) - 1):
            start_city = coordinates[tour[j]]
            end_city = coordinates[tour[j + 1]]
            calculated_cost += euclidean_distance(start_city, end_city)
        
        # Check calculated cost against given cost
        if not math.isclose(calculated_cost, travel_costs[i], abs_tol=1e-6):
            return "FAIL"
        
        overall_travel_cost_calculated += calculated_cost

        # Track visited cities, excluding the depot
        visited_cities.update(tour[1:-1])
    
    # Check all cities visited exactly once
    if len(visited_cities) != num_cities - 1:
        return "FAIL"

    return "CORRECT"

# Robot tours and their respective travel costs provided in the solution
robots_tours = [
    [0, 5, 14, 0], [0, 15, 12, 0], [0, 2, 7, 13, 9, 0], [0, 0],
    [0, 4, 11, 0], [0, 6, 0], [0, 1, 10, 0], [0, 8, 3, 0]
]

travel_costs = [
    62.44277221633522, 66.12407122823275, 78.06088587892982, 0.0,
    57.394073777130664, 24.08318915758459, 41.77216384800009, 72.81785234728197
]

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Run verification
result = verify_solution(robots_tours, travel_costs, coordinates)
print(result)