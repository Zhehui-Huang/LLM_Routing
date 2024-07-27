import math

# Given the position of the cities including the depot
city_positions = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Solution provided
tour_provided = [0, 4, 1, 5, 7, 8, 6, 3, 0]
cost_provided = 307.3737761961791

def check_tour_requirements():
    # Requirement 1: Starts and ends at the depot (city 0)
    if tour_provided[0] != 0 or tour_provided[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly 8 cities
    if len(set(tour_provided)) - 1 != 8:  # Subtract 1 to ignore the repeated depot city
        return "FAIL"

    # Requirement 4: Starts and ends at city 0
    if tour_provided[0] != 0 or tour_provided[-1] != 0:
        return "FAIL"

    # Calculate cost from the tour
    def euclidean_distance(city1, city2):
        return math.sqrt((city_positions[city1][0] - city_positions[city2][0])**2 +
                         (city_positions[city1][1] - city_positions[city2][1])**2)

    total_calculated_cost = sum(euclidean_distance(tour_provided[i], tour_provided[i+1]) 
                                for i in range(len(tour_provided) - 1))

    # Requirement 3 and 5: Correct calculation of the travel cost
    if not math.isclose(total_calculated_cost, cost_provided, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Execute the test
test_result = check_tour_requirements()
print(test_result)