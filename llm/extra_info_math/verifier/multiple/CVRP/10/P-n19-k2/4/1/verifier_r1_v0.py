def test_robot_tours():
    # Example data based on hypothetical output from a VRP solution
    tours = {
        "Robot 0": [0, 1, 2, 0],
        "Robot 1": [0, 3, 4, 0]
    }
    city_demands = {0: 0, 1: 19, 2: 30, 3: 16, 4: 23}
    city_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62)}
    robot_capacity = 160
    cost_matrix = {
        (0, 1): 15, (1, 2): 20, (2, 0): 25,
        (0, 3): 10, (3, 4): 12, (4, 0): 18
    }

    def calculate_travel_cost(tour_list):
        cost = 0
        for i in range(len(tour_list) - 1):
            cost += cost_matrix[(tour_list[i], tour_list[i + 1])]
        return cost
    
    def verify_tours():
        visited_cities = set()
        overall_cost = 0

        for robot, tour in tours.items():
            # Check if each tour begins and ends at the depot
            if tour[0] != 0 or tour[-1] != 0:
                print(f"FAIL: {robot}'s tour does not start or end at depot.")
                return "FAIL"
            
            # Check if total demand on each route does not exceed robot capacity
            total_demand = sum(city_demands[city] for city in tour if city != 0)
            if total_demand > robot_capacity:
                print(f"FAIL: {robot}'s tour exceeds capacity limits.")
                return "FAIL"
            
            # Check if each city is visited once and collect the cities
            for city in tour[1:-1]:  # excluding the depot visit at start and end
                if city in visited_cities:
                    print(f"FAIL: City {city} visited more than once.")
                    return "FAIL"
                visited_cities.add(city)

            # Calculate and accumulate travel costs
            tour_cost = calculate_travel_cost(tour)
            overall_cost += tour_cost
            print(f"{robot} Total Travel Cost: {tour_cost}")

        # Check if all non-depot cities are visited exactly once
        if visited_cities != set(city_demands.keys()) - {0}:
            print("FAIL: Not all cities are visited or some are visited more than once.")
            return "FAIL"

        # If all checks are passed
        print("Overall Total Travel Cost:", overall_cost)
        return "CORRECT"

    result = verify_tours()
    print(result)
    return result

# Call the function to perform the tests
test_robot_tours()