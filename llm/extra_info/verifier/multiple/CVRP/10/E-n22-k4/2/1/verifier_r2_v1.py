import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
        6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
        18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
    }
    demands = {
        0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100, 9: 500, 
        10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100, 17: 1000, 
        18: 900, 19: 2500, 20: 1800, 21: 700
    }
    robot_capacity = 6000

    robots_tours = [
        [0, 1, 2, 3, 4, 6, 7, 8, 9, 0],
        [0, 5, 10, 11, 12, 14, 0],
        [0, 13, 15, 16, 17, 21, 0],
        [0, 18, 19, 20, 0]
    ]
    claimed_costs = [193.17634036562296, 129.78295087540508, 136.08888534674983, 122.22538309272994]
    
    demand_fulfillment = {i: 0 for i in range(1, 22)}
    robot_loads = [0] * 4
    cost_computation = [0] * 4

    for i, tour in enumerate(robots_tours):
        last_city = tour[0]
        for city in tour[1:]:
            distance = calculate_distance(cities[last_city], cities[city])
            cost_computation[i] += distance
            if city != 0:  # Avoid counting the depot
                demand_fulfillment[city] += demands[city]
                robot_loads[i] += demands[city]
            last_city = city
            
    # Check if all demands are exactly met
    if any(demand_fulfillment[city] != demands[city] for city in range(1, 22)):
        return "FAIL - Demand not correctly met"
    
    # Check robot load does not exceed capacity
    if any(load > robot_capacity for load in robot_loads):
        return "FAIL - Capacity exceeded"
    
    # Check if distance calculations are within an acceptable error margin
    if not all(abs(calculated - reported) < 1e-2 for calculated, reported in zip(cost_computation, claimed_costs)):
        return "FAIL - Incorrect travel cost calculations"

    return "CORRECT"

# Run the test function and print result
print(test_solution())