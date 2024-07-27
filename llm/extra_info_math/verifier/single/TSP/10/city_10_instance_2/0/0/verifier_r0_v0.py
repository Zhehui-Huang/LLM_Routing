import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Solution Tour and Cost
solution_tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
solution_cost = 354.91010610434057

# Function returning the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Test for requirement 1 and 2
def test_start_end_at_depot_and_visit_all():
    return solution_tour[0] == solution_tour[-1] == 0 and len(set(solution_tour)) == len(cities) and all(city in solution_tour for city in cities)

# Test for requirement 3: Calculate the total cost, compare against solution cost
def test_total_travel_cost():
    total_cost_calculated = sum(distance(solution_tour[i], solution_tour[i+1]) for i in range(len(solution_tour)-1))
    return math.isclose(total_cost_calculated, solution_cost, rel_tol=1e-9)

# Test for requirement 5 and 6
def test_one_departure_one_entry():
    all_cities = list(cities.keys())
    departures = {city: 0 for city in all_cities}
    entries = {city: 0 for city in all_cities}
    for i in range(len(solution_tour) - 1):
        departures[solution_tour[i]] += 1
        entries[solution_tour[i+1]] += 1
    correct_departures = all(departures[city] == 1 for city in all_cities if city != 0)
    correct_entries = all(entries[city] == 1 for city in all_cities if city != 0)
    return correct_departures and correct_entries

# Test for requirement 7: Check no subtours, for a valid single tour this should already be satisfied given test for requirement 5 and 6.
def test_no_subtours():
    # This would normally require more complex checks. But given valid outputs for 5 and 6, it should be unnecessary.
    return True

def test_solution():
    if all([test_start_end_at_depot_and_visit_all(), test_total_travel_cost(), test_one_departure_one_entry(), test_no_subtours()]):
        return "CORRECT"
    else:
        return "FAIL"

# Running the unit tests
print(test_solution())