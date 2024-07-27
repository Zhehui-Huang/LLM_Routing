import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tours, demands, coordinates, robot_capacity, expected_total_cost):
    city_visited = set()
    total_travel_cost = 0.0
    max_capacity = robot_capacity

    # Coordinates and Demands
    coordinates_dict = {i: coord for i, coord in enumerate(coordinates)}
    demand_dict = {i: d for i, d in enumerate(demands)}
    
    for tour in tours:
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        current_load = 0
        last_city = tour[0]
        
        for city in tour[1:]:
            city_visited.add(city)
            # Calculate travel cost
            total_travel_cost += euclidean_distance(*coordinates_dict[last_city], *coordinates_dict[city])
            # Add demands to check capacity constraints
            current_load += demand_dict[city]
            if current_load > max_capacity:
                return "FAIL"
            last_city = city
        
        # Closing the loop back to the depot
        total_travel_cost += euclidean_distance(*coordinates_dict[last_city], *coordinates_dict[tour[0]])
    
    # Check if all non-depot cities are visited and the total cost is minimal
    if city_visited != set(range(1, len(coordinates))) or not math.isclose(total_travel_cost, expected_total_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Data
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
               (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
               (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
robot_capacity = 6000

# Tours and costs
tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],  # Robot 0
    [0, 14, 16, 17, 20, 21, 8, 0],  # Robot 1
    [0, 14, 16, 17, 20, 21, 8, 0],  # Robot 2
    [0, 14, 16, 17, 20, 21, 8, 0]   # Robot 3
]
expected_total_cost = 542.5289951743111

# Run verification
result = verify_solution(tours, demands, coordinates, robot_capacity, expected_total_cost)
print(result)