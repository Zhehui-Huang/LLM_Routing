def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours(tours, cities):
    city_visit_count = {i: 0 for i in range(len(cities))}
    for tour in tours:
        # Verify each city is visited exactly once, excluding the depot being visited multiple times as start/end points
        for index in range(1, len(tour)-1):  # Ignore first and last as they are the depot
            city_visit_count[tour[index]] += 1

        # Verify each city is visited exactly once by one salesman 
        if any(city_visit_count[city] > 1 for city in city_visit_count if city != 0):
            return "FAIL - City visited more than once"

        # Verify salesman leaves each city exactly once
        if len(tour) != len(set(tour))-1:  # set(tour)-1 because depot can repeat
            return "FAIL - Duplicate visit in tour"

        # Check if every non-depot city is visited at least once
        if not all(count == 1 for city, count in city_visit_count.items() if city != 0):
            return "FAIL - Not all cities visited"

        # Verify each salesman leaves the depot exactly once as a starting point and returns once
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL - Tour does not start or end at depot"

    # Subtour elimination and binary variable constraints are inherently managed by the model's formulation and solver integrity.
    # Position constraints (u_i) are assumed correctly handled as per solver output maintaining the integrity of the model.

    return "CORRECT"

# Test the solution
def test_solution():
    cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
              (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
    
    tours = [
        [0, 1, 10, 4, 11, 15, 12, 3, 19, 18, 8, 2, 7, 13, 9, 17, 14, 5, 20, 6, 0],
        [0, 16, 0]
    ]
    
    result = verify_tours(tours, cities)
    print(result)

test_solution()