import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_solution():
    # Coordinates of the cities
    cities = [
        (8, 11),  # City 0
        (40, 6),  # City 1
        (95, 33),  # City 2
        (80, 60),  # City 3
        (25, 18),  # City 4
        (67, 23),  # City 5
        (97, 32),  # City 6
        (25, 71),  # City 7
        (61, 16),  # City 8
        (27, 91),  # City 9
        (91, 46),  # City 10
        (40, 87),  # City 11
        (20, 97),  # City 12
        (61, 25),  # City 13
        (5, 59),  # City 14
        (62, 88),  # City 15
        (13, 43),  # City 16
        (61, 28),  # City 17
        (60, 63),  # City 18
        (93, 15)   # City 19
    ]
    
    # Provided solution details
    tour_provided = [0, 12, 6, 1, 0]
    total_cost_provided = 282.64

    # Test length of the tour
    if len(tour_provided) != 5 or tour_provided[0] != 0 or tour_provided[-1] != 0:
        return "FAIL"

    # Test number of unique cities (excluding the repeated city 0 at the end)
    if len(set(tour_provided[:-1])) != 4:
        return "FAIL"

    # Test if only the first city and the last city are the depot
    if tour_provided[0] != 0 and tour_provided[-1] != 0:
        return "FAIL"

    # Calculate cost
    total_cost_calculated = 0
    for i in range(len(tour_provided) - 1):
        total_cost_calculated += euclidean_distance(cities[tour_provided[i]], cities[tour_provided[i+1]])

    # Round the computed cost to two decimal places
    total_cost_calculated = round(total_cost_calculated, 2)

    # Check if the calculated total cost matches the provided total cost
    if abs(total_cost_calculated - total_cost_provided) > 0.01:  # Allowing some leeway for floating-point precision issues
        return "FAIL"

    return "CORRECT"

# Running the test function
output = test_tsp_solution()
print(output)