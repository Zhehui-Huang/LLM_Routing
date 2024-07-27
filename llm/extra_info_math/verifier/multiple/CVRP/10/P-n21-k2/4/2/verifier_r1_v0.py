def is_at_depot(route):
    return route[0] == 0 and route[-1] == 0

def unique_visits(tours):
    visited = set()
    for tour in tours:
        visited.update(tour[1:-1])  # exclude depot city from each route for counting
    return len(visited) == 20  # since there are 20 cities (excluding the depot)

def capacity_check(tours, demands, capacity):
    for tour in tours:
        total_demand = sum(demands[city] for city in tour[1:-1])  # calculate total demand per tour excluding depot
        if total_demand > capacity:
            return False
    return True

def calculate_cost(route, coordinates):
    cost = 0
    for i in range(len(route) - 1):
        x1, y1 = coordinates[route[i]]
        x2, y2 = coordinates[route[i + 1]]
        cost += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(cost, 2)

def check_solution():
    # Constants from problem statement
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
    coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
                   (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
                   (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
    capacity = 160

    # Tours provided
    tours = [
        [0, 2, 8, 17, 4, 6, 14, 7, 0], 
        [0, 18, 3, 20, 12, 16, 5, 15, 9, 10, 1, 11, 13, 19, 0]
    ]
    
    # Costs provided
    provided_costs = [182.33, 381.19]
    calculated_costs = [calculate_cost(tour, coordinates) for tour in tours]

    # Checking routes start and end at the depot and costs
    if not all(is_at_depot(tour) for tour in tours):
        return "FAIL"
    if not all(provided_costs[i] == calculated_costs[i] for i in range(len(provided_costs))):
        return "FAIL"
    if not unique_visits(tours):
        return "FAIL"
    if not capacity_check(tours, demands, capacity):
        return "FAIL"

    # Since all checks passed
    return "CORRECT"

# Test and print result
print(check_solution())