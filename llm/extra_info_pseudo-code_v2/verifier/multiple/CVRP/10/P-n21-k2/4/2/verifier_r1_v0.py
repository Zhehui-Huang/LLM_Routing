import math

# Provided tour and costs data
robot_tours = {
    0: ([0, 8, 18, 0], 78.92915028151745),
    1: ([0, 14, 19, 0], 89.96025639847296)
}
overall_total_cost = 168.88940667999043

# Coordinates and demands data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
]
capacity_per_robot = 160

def calculate_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def test_correctness(tours, coordinates, demands, capacity):
    total_calculated_cost = 0
    delivered = [0] * len(coordinates)
    
    for robot, (tour, reported_cost) in tours.items():
        # Start and end at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        total_tour_demand = 0
        calculated_cost = 0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            distance = calculate_distance(coordinates[city_from], coordinates[city_to])
            calculated_cost += distance
            
            # Only add demand for non-depot cities
            if city_to != 0:
                total_tour_demand += demands[city_to]
                delivered[city_to] += demands[city_to]
        
        # Check robot load and cost calculation
        if total_tour_demand > capacity or not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"
        
        total_calculated_cost += calculated_cost
    
    # Check demand fulfillment and overall cost
    if any(d != deliver for d, deliver in zip(demands, delivered)) or not math.isclose(total_calculated_cost, overall_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = test_correctness(robot_tours, coordinates, demands, capacity_per_robot)
print(result)