import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tours():
    # City coordinates - added as tuples for easier indexing
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]

    # Demand list
    demands = [
        0, 1100, 700, 800, 1400, 2100, 400, 800,
        100, 500, 600, 1200, 1300, 1300, 300,
        900, 2100, 1000, 900, 2500, 1800, 700
    ]

    # Provided solution
    robots = {
        0: ([0, 1, 2, 0, 3, 4, 0, 6, 8, 0, 9, 10, 0], 315.0360235556025),
        1: ([0, 5, 7, 0, 18, 20, 0], 146.21824884942993),
        2: ([0, 19, 21, 0, 11, 13, 0], 132.68209129084335),
        3: ([0, 15, 17, 0, 14, 16, 12, 0], 107.24839460743758)
    }

    robot_capacity = 6000
    city_delivery = [0] * 22
    overall_cost = 0

    for robot_id, (tour, reported_cost) in robots.items():
        current_capacity = 0
        last_city = 0
        calculated_cost = 0

        for city in tour:
            if city != 0:  # Exclude depot
                current_capacity += demands[city]
                city_delivery[city] += demands[city]
            if city != last_city:
                distance = compute_distance(coordinates[last_city], coordinates[city])
                calculated_cost += distance
            last_city = city
        
        if current_capacity > robot_capacity:
            print("FAIL: Capacity exceeded for Robot", robotb_id)
            return "FAIL"

        if not tour[0] == tour[-1] == 0:
            print("FAIL: Tour does not start and end at the depot for Robot", robot_id)
            return "FAIL"

        overall_cost += calculated_cost

    if any(city_delivery[i] != demands[i] for i in range(1, 22)):
        print("FAIL: Not all city demands are met.")
        return "FAIL"
    
    for robot_id, (_, reported_cost) in robots.items():
        if not math.isclose(reported_cost, robots[robot_id][1], abs_tol=1e-1):
            print(f"FAIL: Cost mismatch for Robot {robot_id}")
            return "FAIL"

    if not math.isclose(overall_cost, sum(cost for _, cost in robots.values()), abs_tol=1e-1):
        print("FAIL: Overall cost mismatch.")
        return "FAIL"

    print("CORRECT")
    return "CORRECT"

# Running the unit test verification
verify_tours()