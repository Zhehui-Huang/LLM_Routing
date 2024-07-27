def test_solution():
    # Robot tours as described in the solution
    robot_tours = {
        0: [0, 3, 1, 0],
        1: [0, 2, 0],
        2: [0, 4, 5, 0],
        3: [0, 6, 0],
        4: [0, 7, 10, 9, 0],
        5: [0, 8, 11, 0],
        6: [0, 12, 15, 13, 0],
        7: [0, 14, 0]
    }
    
    # Demand for each city
    city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
    
    # Capacity of each robot
    robot_capacity = 35
    
    visited = set()
    all_cities = set(range(1, 16))

    for robot, tour in robot_tours.items():
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return
        
        # Check demands
        total_demand = 0
        for city in tour[1:-1]:  # exclude the depot at start and end
            total_demand += city_demands[city]
            visited.add(city)
        
        if total_demand > robot_capacity:
            print("FAIL")
            return
            
    # Check if all cities are visited exactly once
    if visited != all_cities:
        print("FAIL")
        return
    
    print("CORRECT")

# Run the test function
test_solution()