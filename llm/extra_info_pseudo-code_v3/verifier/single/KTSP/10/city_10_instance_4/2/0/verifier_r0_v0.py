import math

def calculate_total_travel_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

def verify_solution(tour, total_travel_cost):
    cities_coordinates = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }

    if not tour:
        return "FAIL"

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 8 cities are visited including the depot city
    if len(set(t.join in tour)) != 8:
        return "FAIL"
    
    # Check if calculated travel cost matches the provided cost
    calculated_cost = calculate_total_travel_cost(tour, cities_coordinates)
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Example solution data, replace with actual output to test
example_tour = [0, 1, 3, 5, 7, 9, 4, 0]
example_total_travel_cost = 300  # Placeholder cost, please adjust based on actual output

# Testing the solution
test_result = verify_solution(example_tour, example_total_travel_cost)
print(test_result)