import math

# Define the city coordinates and demands
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Define tours and their reported costs
tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
    [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
]
tours_costs = [135.56632457243472, 160.8323261436827]
robot_capacity = 160

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = city_coordinates[tour[i - 1]]
        x2, y2 = city_coordinates[tour[i]]
        total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_cost

def check_route_demands_and_capacity(tour):
    total_demand = sum(city_demands[city] for city in tour[1:-1])  # Exclude depot
    return total_demand <= robot_capacity, total_demand

def test_solution(tours, tours_costs):
    correct = True
    total_computed_cost = 0

    for idx, tour in enumerate(tours):
        calculated_cost = calculate_cost(tour)
        cost_close = math.isclose(calculated_cost, tours_costs[idx], rel_tol=1e-5)
        valid_capacity, demand = check_route_demands_and_capacity(tour)

        print(f"Robot {idx} Tour: {tour}")
        print(f"Calculated Cost: {calculated_cost}, Expected Cost: {tours_costs[idx]}, Cost Match: {'PASS' if cost_close else 'FAIL'}")
        print(f"Capacity Check (Demand: {demand}, Capacity: {robot_capacity}): {'PASS' if valid_capacity else 'FAIL'}")

        total_computed_cost += calculated_cost
        correct &= cost_close and valid_capacity

    overall_cost_close = math.isclose(total_computed_cost, sum(tours_costs), rel_tol=1e-5)
    print(f"Overall Cost: {total_computed_cost}, Expected Overall: {sum(tours_costs)}, Overall Match: {'PASS' if overall_cost_close else 'FAIL'}")

    return "CORRECT" if correct and overall_cost_close else "FAIL"

# Execute tests
result = test_solution(tours, tours_costs)
print(result)