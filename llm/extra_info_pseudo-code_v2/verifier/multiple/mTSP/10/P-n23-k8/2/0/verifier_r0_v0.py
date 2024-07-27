import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def test_solution():
    # City coordinates, including the depot
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
        (45, 35), (32, 39), (56, 37)
    ]
    
    # Tours provided in the solution
    tours = [
        [0, 1, 2, 0],
        [0, 3, 4, 0],
        [0, 5, 6, 0],
        [0, 7, 8, 0],
        [0, 9, 10, 0],
        [0, 11, 12, 0],
        [0, 13, 14, 0],
        [0, 16, 15, 19, 18, 17, 22, 20, 21, 0]
    ]
    
    # Checking the number of robots
    if len(tours) != 8:
        return "FAIL"
    
    # Check for all cities visited exactly once excluding the depot
    all_visited_cities = set()
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:
            if city in all_visited_cities or city == 0:
                return "FAIL"
            all_visited_cities.add(city)
    
    if len(all_visited_cities) != len(cities) - 1:
        return "FAIL"
    
    # Calculate and verify travel costs
    provided_costs = [47.29, 75.68, 47.93, 72.19, 77.87, 74.16, 80.99, 128.54]
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_costs.append(round(cost, 2))
    
    if calculated_costs != provided_costs:
        return "FAIL"
    
    # Verify the overall cost
    overall_cost = sum(provided_costs)
    if not math.isclose(overall_cost, 604.65, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = test_solution()
print(result)