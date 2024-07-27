import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def evaluate_solution(data):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69)
    }
    visits = set(range(1, 16))  # cities to be visited (exclude depot)
    robot_start_end = 0  # all robots start and end at depot city 0
    total_cities = 16
    num_robots = 8

    max_cost = 0
    # Collect all city visits to check the constraint of visiting each city exactly once
    all_city_visits = set()

    # Check all tour constraints
    for robot_tour in data:
        tour, tour_cost = robot_tour
        calculated_cost = 0

        if tour[0] != robot_start_end or tour[-1] != robot_start_end:
            print("Robot tour does not start and end at the depot.")
            return "FAIL"
        
        for i in range(1, len(tour)):
            city_from = tour[i - 1]
            city_to = tour[i]
            step_cost = distance(cities[city_from], cities[city_to])
            calculated_cost += step_cost
            all_city_visits.add(city_to)

        if abs(calculated_cost - tour_cost) > 1e-6:
            print(f"Mismatch in reported and calculated cost for tour {tour}.")
            return "FAIL"
        
        max_cost = max(max_cost, calculated_cost)

    if visits != all_city_visits:
        print("Not all cities are visited exactly once or some cities are visited multiple times.")
        return "FAIL"

    return "CORRECT"

# Test data from the provided solution
tours = [
    ([0, 6, 0], 24.08318915758459),
    ([0, 1, 3, 0], 65.65945789394776),
    ([0, 10, 12, 0], 60.8251757953491),
    ([0, 2, 13, 8, 0], 72.57901828006285),
    ([0, 4, 15, 0], 61.07512778319072),
    ([0, 7, 9, 0], 64.13503025042893),
    ([0, 5, 14, 0], 62.44277221633522),
    ([0, 11, 0], 56.32051136131489)
]

# Call the function to evaluate the correctness of the solution provided
result = evaluate_solution(tours)
print(result)