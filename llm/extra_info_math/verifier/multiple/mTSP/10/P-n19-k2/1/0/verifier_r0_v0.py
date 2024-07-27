def verify_solution(tours, costs):
    cities = set(range(1, 19))  # City index starts from 1 to 18, excluding the depot 0
    visited_cities = set()
    depot_visits = [0 for _ in range(len(tours))]  # Count the number of times each robot leaves the depot
    
    for robot_index, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Each tour should start and end at the depot city 0
        
        depot_visits[robot_index] += 1  # Each robot leaves the depot
        
        # Check if each city is visited exactly once by one salesman and track visited cities
        for city in tour[1:-1]:  # Skip the depot at the start and end
            if city in visited_cities:
                return "FAIL"  # City visited more than once across tours
            visited_cities.add(city)
            
        # Check if tour has no subtours and if each city in the tour is visited once by this salesman
        for i in range(1, len(tour) - 1):
            if tour[i] == tour[i+1]:
                return "FAIL"  # Next city is the same as current, which shouldn't happen

    if visited_cities != cities:
        return "FAIL"  # Not all cities were visited exactly once

    if any(v != 1 for v in depot_visits):
        return "FAIL"  # Each robot must leave the depot exactly once

    return "CORRECT"

# Given solution's output
robot0_tour = [0, 6, 0]
robot1_tour = [0, 18, 2, 7, 5, 13, 15, 9, 8, 16, 17, 3, 12, 14, 11, 4, 10, 1, 0]

robot0_cost = 24.08318915758459
robot1_cost = 168.72893710897952
overall_cost = 192.81212626656412

tours = [robot0_tour, robot1_tour]
costs = [robot0_cost, robot1_cost, overall_cost]

# Verify solution against requirements
verification_result = verify_solution(tours, costs)
print(verification_result)