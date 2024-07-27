import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, costs, max_cost):
    # Coordinates of cities including the depot
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    cities_visited = set()
    computed_costs = []
    
    # Check if each tour starts and ends at the depot (city 0), and aggregate visited cities
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot"
        cities_visited.update(tour)
        
        # Calculate the travel cost for the tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        computed_costs.append(tour_cost)
    
    # Check if all cities are visited exactly once, excluding the depot
    if cities_visited != set(range(19)):
        return "FAIL: Not all cities visited or some cities are visited more than once"
    
    # Check if the tour costs match computed costs
    if not all(math.isclose(computed_costs[i], costs[i], rel_tol=1e-9) for i in range(len(tours))):
        return "FAIL: Reported travel costs do not match the computed costs"
    
    # Check the maximum cost
    if not math.isclose(max(computed_costs), max_cost, rel_tol=1e-9):
        return "FAIL: Maximum travel cost is incorrect"
    
    return "CORRECT"

# Example usage
tours = [
    [0, 6, 18, 10, 7, 11, 12, 15, 8, 16, 0],
    [0, 1, 2, 4, 5, 14, 13, 9, 3, 17, 0]
]
costs = [222.91725734243755, 272.5324816435078]
max_cost = 272.5324816435078

print(verify_solution(tours, costs, max_cost))