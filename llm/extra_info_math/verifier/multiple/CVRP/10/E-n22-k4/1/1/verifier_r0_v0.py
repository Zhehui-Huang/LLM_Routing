def calculate_travel_cost(route, coordinates):
    total_cost = 0
    for i in range(len(route) - 1):
        start, end = route[i], route[i + 1]
        dist = ((coordinates[start][0] - coordinates[end][0])**2 + (coordinates[start][1] - coordinates[end][1])**2)**0.5
        total_cost += dist
    return total_cost

def verify_solution(tours, demands, capacities, coordinates):
    visited_cities = set()
    total_calculated_cost = 0
    robot_capacity = 6000

    for robot_id, tour in enumerate(tours):
        # Check if starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check if each city visited once and calculate demand
        current_load = 0
        for city in tour[1:-1]:  # exclude starting and ending depot
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
            current_load += demands[city]

        # Check load doesn't exceed capacity
        if current_load > capacities[robot_id]:
            return "FAIL"
        
        # Calculate and sum costs
        calculated_cost = calculate_travel_cost(tour, coordinates)
        if calculated_cost != 0:  # Given total travel cost is 0 in the problem's solution
            return "FAIL"
        total_calculated_cost += calculated_cost

    # Check if all cities are visited
    if len(visited_cities) != len(demands) - 1:
        return "FAIL"
    
    # Check if the overall travel cost is correct
    if total_calculated_cost != 0:
        return "FAIL"

    return "CORRECT"

# Given data
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacities = [6000, 6000, 6000, 6000]
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]

# Tours from problem's solution
tours = [
    [0, 5, 3, 2, 1, 0],
    [0, 12, 11, 10, 9, 7, 4, 0],
    [0, 17, 16, 15, 14, 13, 6, 0],
    [0, 21, 20, 19, 18, 8, 0]
]

# Run tests
result = verify_solution(tours, demands, capacities, coordinates)
print(result)