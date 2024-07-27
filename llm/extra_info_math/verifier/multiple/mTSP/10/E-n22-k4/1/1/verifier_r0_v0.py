# Provided solution data
robot_tours = {
    0: [0, 14, 0],
    1: [0, 16, 0],
    2: [0, 15, 18, 20, 17, 21, 19, 13, 11, 4, 3, 1, 2, 5, 7, 9, 6, 8, 10, 0],
    3: [0, 12, 0]
}

# Total cities including the depot
total_cities = set(range(22))  # cities 0 to 21

def verify_cities_visited_once():
    visited_cities = set()
    for tour in robot_tours.values():
        for city in tour[1:-1]:  # Excluding the initial and final depot visit
            if city in visited_cities:
                return False
            visited_cities.add(city)
    # Check if all cities except depot are visited
    return visited_cities == total_cities - {0}

def verify_flow_conservation():
    for tour in robot_tours.values():
        # Excluding depots, each city should appear exactly once
        cities = tour[1:-1]
        if len(cities) != len(set(cities)):
            return False
    return True

def verify_each_salesman_leaves_depot_once():
    for tour in robot_tours.values():
        if tour.count(0) != 2:  # Each tour should start and end at 0
            return False
    return True

def check_solution():
    if not verify_cities_visited_once():
        return "FAIL"
    if not verify_flow_conservation():
        return "FAIL"
    if not verify_each_salesman_leaves_depot_once():
        return "FAIL"
    return "CORRECT"

# Running the test
result = check_solution()
print(result)