import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two coordinates """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours(robot_tours, cities, depots):
    # Verify Requirement 1
    for robot_id, tour in enumerate(robot_tours):
        if tour[0] != depots[robot_id] or tour[-1] != depots[robot_id]:
            return "FAIL"
    
    # Verify Requirement 2
    city_visits = [0] * len(cities)
    for tour in robot_tours:
        for city in tour[1:-1]:  # ignore starting and ending depot in count
            city_visits[city] += 1
    
    if any(v > 1 for v in city_visits) or any(v == 0 for i, v in enumerate(city_visits) if i not in depots):
        return "FAIL"
    
    # Verify Requirement 3: Check provided travel costs
    provided_costs = [
        107.91301489389802,  # Should be the cost sum of robot 0 tour cities
        107.91301489389802   # Should be the cost sum of robot 1 tour cities
    ]

    calculated_costs = []
    for tour in robot_tours:
        total_cost = 0
        for i in range(1, len(tour)):
            total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        calculated_costs.append(total_cost)

    if not all(math.isclose(provided, calculated, abs_tol=0.0001) 
               for provided, calculated in zip(provided_costs, calculated_costs)):
        return "FAIL"

    return "CORRECT"

# Define city coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

depots = [0, 1]

robot_tours = [
    [0, 6, 5, 7, 2, 8, 3, 4, 1, 0],
    [1, 4, 14, 12, 11, 10, 15, 9, 16, 17, 18, 13, 1]
]

result = verify_tours(robot_tours, cities, depots)
print(result)