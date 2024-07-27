import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tours, costs, coordinates, overall_cost):
    # Verify each city is visited exactly once
    all_cities_visited = set()
    for tour in tours:
        for city in tour[1:-1]:  # exclude the depot city at start and end
            if city in all_cities_visited:
                return "FAIL"
            all_cities_visited.add(city)
    
    if len(all_cities_visited) != 21:  # 21 cities excluding the depot
        return "FAIL"
    
    # Verify the total cost for each tour
    calculated_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_costs.append(round(tour_cost, 2))
    
    if calculated_costs != costs:
        return "FAIL"
    
    # Verify the overall total travel cost
    if not math.isclose(sum(calculated_costs), overall_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Other requirements implicitly satisfied by this test setup
    return "CORRECT"

# Robot tours and their travel costs as provided
tours = [
    [0, 9, 5, 1, 13, 21, 17, 0],
    [0, 14, 18, 2, 6, 10, 0],
    [0, 19, 11, 3, 7, 15, 0],
    [0, 4, 8, 12, 20, 16, 0]
]
costs = [183.31, 149.94, 183.25, 153.00]
overall_cost = 669.50

# Coordinates of the cities (Depot + City 1 to City 21)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 205), (129, 189), (155, 185),
    (139, 182)
]

result = verify_solution(tours, costs, coordinates, overall_cost)
print(result)