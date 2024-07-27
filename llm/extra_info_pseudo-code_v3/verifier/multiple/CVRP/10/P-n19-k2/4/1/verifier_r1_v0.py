import math

def calculate_euclidean_distance(from_city, to_city):
    return math.sqrt((from_city[0] - to_city[0]) ** 2 + (from_city[1] - to_city[1]) ** 2)

def check_solution_correctness():
    # City coordinates
    city_coords = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
        (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    # City demands
    city_demands = {
        0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 
        10: 8, 11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
    }

    # Robot tours
    tours = {
        0: [0, 9, 7, 13, 5, 15, 11, 18, 14, 6, 17, 0],
        1: [0, 1, 2, 8, 16, 10, 3, 12, 4, 0]
    }

    # Test travel costs reported
    reported_costs = {
        0: 303.52,
        1: 130.56
    }

    # Robot capacity
    max_capacity = 160

    # Testing demands are met and capacities are not exceeded
    for robot, tour in tours.items():
        capacity_used = 0
        last_city_index = 0
        calculated_cost = 0
        visited_demands = {}

        for city_index in tour:
            if city_index != 0:  # Depot has no demand and should not count to capacity
                if city_index in visited_demands:
                    return "FAIL"  # City visited more than once excluding the depot
                visited_demands[city_index] = True
                capacity_used += city_demands[city_index]
                if capacity_used > max_capacity:
                    return "FAIL"
            
            # Calculate travel cost
            if last_city_index != city_index:  # Skip if same city repeated
                calculated_cost += calculate_euclidean_distance(city_coords[last_city_index], city_coords[city_index])
                last_city_index = city_index
        
        # Check if all costs are correctly reported (allow small float error range)
        if not math.isclose(calculated_cost, reported_costs[robot], abs_tol=0.01):
            return "FAIL"
    
    # Check all cities are visited exactly once except depot (0)
    all_visited_cities = set(city for tour in tours.values() for city in tour if city != 0)
    if len(all_visited_cities) != len(city_demands) - 1:  # -1 to exclude the depot
        return "FAIL"

    # Check if the start and end of each tour is depot (0)
    if any(tour[0] != 0 or tour[-1] != 0 for tour in tours.values()):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Execute the test
print(check_solution_correctness())