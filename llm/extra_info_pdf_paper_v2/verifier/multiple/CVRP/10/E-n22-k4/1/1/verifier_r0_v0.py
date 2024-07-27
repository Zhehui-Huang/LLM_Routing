def test_robot_tours():
    # Given test results
    robot_tours = [
        {"tour": [0], "cost": 0.00},
        {"tour": [0], "cost": 0.00}, 
        {"tour": [0], "cost": 0.00}, 
        {"tour": [0], "cost": 0.00}
    ]
    overall_cost = 0.00

    # Requirement 1: Each robot must start and end its tour at the depot city (city 0)
    requirement_1_passed = all(tour['tour'][0] == 0 and tour['tour'][-1] == 0 for tour in robot_tours)

    # City demands from the problem description
    demands = {
        1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 
        8: 100, 9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 
        15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700
    }
    delivered = {key: 0 for key in demands.keys()}  # Tracker for delivered quantities to each city

    # Capacity of each robot
    robot_capacity = 6000

    # Check demand delivery and robot capacity
    for robot in robot_tours:
        tour = robot['tour']
        tour_cost = robot['cost']
        load = 0
        for i in range(1, len(tour)):
            city = tour[i]
            if city != 0:  # City 0 is the depot, no delivery
                delivered[city] += demands[city]  # Assume entire demand must be met per city exactly once
                load += demands[city]
    
    # Requirement 2: Each city's demand must be fully met by the collective deliveries of the robots
    requirement_2_passed = all(delivered[key] == demands[key] for key in demands)

    # Requirement 3: The carrying capacity of each robot must not be exceeded
    requirement_3_passed = all(load <= robot_capacity for load in [sum(demands[tour[i]] if i != 0 else 0 for i in range(1, len(tour))) for robot in robot_tours for tour in [robot['tour']]])

    # Requirement 4: Minimize the total travel cost - this test is qualitative and would need actual route data to compare if optimized
    # Here we just check if the cost given and computed overall cost match:
    requirement_4_passed = overall_cost == sum(robot['cost'] for robot in robot_tours)

    # Requirement 5 and 6 are output requirements ensured by the output described in the problem
    output_requirements_passed = all('tour' in robot and 'cost' in robot for robot in robot_tours)

    if requirement_1_passed and requirement_2_passed and requirement_3_passed and requirement_4_passed and output_requirements_passed:
        return "CORRECT"
    else:
        return "FAIL"

# Outputting the test suite results
print(test_robot_tours())  # Should output "FAIL" because no actual tours delivering the goods are reported nor the correct costs are shown.