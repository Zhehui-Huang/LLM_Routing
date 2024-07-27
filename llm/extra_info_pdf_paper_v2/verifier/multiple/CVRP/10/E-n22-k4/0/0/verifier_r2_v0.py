from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, demands, coordinates, capacities):
    total_demand = sum(demands)
    delivered = [0] * len(demands)
    total_delivered = 0
    total_travel_cost = 0
    
    for robot, tour in enumerate(tours):
        # Check if tour starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        current_load = 0
        last_city = tour[0]
        for city in tour[1:]:
            current_load += demands[city]
            if current_load > capacities:
                return "FAIL"
            total_travel_cost += calculate_distance(coordinates[last_city], coordinates[city])
            delivered[city] += demands[city]
            total_delivered += demands[city]
            last_city = city
    
    if total_delivered != total_demand or any(d != demands[i] for i, d in enumerate(delivered)):
        return "FAIL"
    
    # Provided total cost calculated in the given solution:
    provided_total_cost = 135.63 + 163.95 + 165.66 + 124.18
    
    # Check if calculated total travel cost matches with provided total travel cost roughly
    if not (abs(total_travel_cost - provided_total_cost) <= 1):  # allowing small floating-point errors
        return "FAIL"
    
    return "CORRECT"

# Define coordinates and demands as per the problem statement
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400,
           2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300,
           900, 2100, 1000, 900, 2500,
           1800, 700]
robot_capacity = 6000

# Tours and travel costs are given as follows:
tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 12, 15, 18, 19, 6, 0],
    [0, 13, 11, 10, 9, 7, 2, 3, 0],
    [0, 5, 1, 4, 0]
]

# Test the solution
print(verify_solution(tours, demands, coordinates, robot_capacity))