import math

# City coordinates and demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 7},
    2: {'coord': (49, 49), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 19},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 8},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 48), 'demand': 6},
    14: {'coord': (58, 27), 'demand': 19},
    15: {'coord': (37, 69), 'demand': 11},
    16: {'coord': (38, 46), 'demand': 12},
    17: {'coord': (61, 33), 'demand': 26},
    18: {'coord': (62, 63), 'demand': 17},
    19: {'coord': (63, 69), 'demand': 6},
    20: {'coord': (45, 35), 'demand': 15},
    21: {'coord': (32, 39), 'demand': 5},
    22: {'coord': (56, 37), 'demand': 10}
}

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Robot tours and costs provided in the solution
robot_tours = [
    [0, 1, 2, 0], [0, 3, 4, 17, 0], [0, 5, 6, 18, 0], 
    [0, 7, 19, 20, 0], [0, 8, 9, 21, 0], [0, 10, 11, 12, 13, 22, 0], 
    [0, 14, 15, 0], [0, 16, 0]
]
robot_costs = [47.28555690793142, 127.15845355611994, 105.03329972120916, 106.38808988271246, 
               81.59871093427857, 117.00122824422864, 107.66099338871445, 20.0]

# Check if the solution is correct
def verify_solution(tours, costs, robot_capacity=40):
    total_cost = 0
    demands = {i: 0 for i in range(23)}  # Initialize demand satisfaction
    
    for tour, cost in zip(tours, costs):
        demand_in_tour = 0
        computed_cost = 0
        prev_city = 0
        
        for city in tour:
            if city != 0:  # Avoid computing demand for depot
                demands[city] += cities[city]['demand']
                demand_in_tour += cities[city]['demand']
            
            # Compute travel cost
            if prev_city is not None:
                travel_cost = calculate_distance(cities[prev_city]['coord'], cities[city]['coord'])
                computed_cost += travel_cost
            prev_city = city
        
        # Check capacity and tour cost
        if demand_in_tour > robot_capacity or not math.isclose(computed_cost, cost, abs_tol=0.0001):
            return "FAIL"
        
        total_cost += cost

    # Demand satisfaction check
    if any(cities[i]['demand'] != demands[i] for i in cities):
        return "FAIL"
    
    # Total cost comparison
    if not math.isclose(total_cost, sum(costs), abs_tol=0.0001):
        return "FAIL"
    
    return "CORRECT"

# Output result of verification
result = verify_solution(robot_tours, robot_costs)
print(result)