import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution():
    # City coordinates as per the problem description
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
        (62, 63), (63, 69), (45, 35)
    ]
    # Demand as per the problem description
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
    
    # Tours provided in the solution
    tours = [
        [0, 16, 6, 1, 10, 2, 4, 11, 15, 12, 8, 0],
        [0, 20, 7, 5, 13, 14, 17, 9, 3, 18, 19, 0]
    ]
    capacities = [160, 160]
    
    # Check if all cities except depot are visited at least once
    all_visited = set(j for tour in tours for j in tour[1:-1])
    if all_visited != set(range(1, 21)):
        return "FAIL"
    
    # Check if any city is served more than once
    unique_visits = []
    for tour in tours:
        for city in tour[1:-1]:
            if city in unique_visits:
                return "FAIL"
            unique_visits.append(city)

    # Check load and compute travel costs
    travel_costs = []
    for i, tour in enumerate(tours):
        total_demand = 0
        total_distance = 0
        for j in range(len(tour) - 1):
            city1 = tour[j]
            city2 = tour[j+1]
            total_demand += demands[city2]
            total_distance += calculate_distance(cities[city1], cities[city2])
        if total_demand > capacities[i]:
            return "FAIL"
        travel_costs.append(total_distance)
    
    # Total travel cost computed in the test should match the provided total
    provided_total_cost = 311.25031071721776
    calculated_total_cost = sum(travel_costs)
    if not math.isclose(provided_total_cost, calculated_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(check_solution())