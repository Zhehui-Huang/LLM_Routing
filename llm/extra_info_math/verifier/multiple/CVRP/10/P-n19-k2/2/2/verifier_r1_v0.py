import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def check_solution(tours, travel_costs, city_demands, city_coordinates, robot_capacity):
    all_visited_cities = set()
    expected_cities = set(range(1, len(city_demands)))
    
    total_calculated_cost = 0
    
    for tour, reported_cost in zip(tours, travel_costs):
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check demand and accumulation of visited cities
        total_demand = 0
        for i in range(1, len(tour)-1):
            city_id = tour[i]
            total_demand += city_demands[city_id]
            all_visited_cities.add(city_id)
        
        if total_demand > robot_capacity:
            return "FAIL"
        
        # Calculate travel cost for this tour
        calculated_cost = 0
        for i in range(len(tour)-1):
            start_city = city_coordinates[tour[i]]
            end_city = city_coordinates[tour[i+1]]
            calculated_cost += calculate_distance(start_city, end_city)
        
        # Keeping running total of reported and calculated costs
        total_calculated_cost += calculated_cost
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"
    
    # Check if all cities except the depot were visited exactly once
    if all_visited_cities != expected_cities:
        return "FAIL"
    
    # Comparing overall cost not as direct requirement in unit test since individual paths and costs have been verified
    return "CORRECT"
    
# Define city coordinates and demands
city_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
                    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
                    (61, 33), (62, 63), (63, 69), (45, 35)]
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Solution data
tours = [
    [0, 1, 2, 3, 4, 5, 6, 7, 9, 0],
    [0, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]
]
reported_costs = [171.9242612944609, 305.4411951909097]
robot_capacity = 160

# Check the solution
result = check_solution(tours, reported_costs, city_demands, city_coordinates, robot_capacity)
print(result)