import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Define the cities as per the task description
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
    
    # Solution as provided
    tour = [0, 8, 5, 2, 1, 9, 0]
    total_travel_cost = 183.85354044487238

    # Check the tour length and inclusion of cities
    if len(tour) != 7 or len(set(tour)) != 7:
        return "FAIL"
    
    # Check that the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that the robot visits exactly 6 cities
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_solution())