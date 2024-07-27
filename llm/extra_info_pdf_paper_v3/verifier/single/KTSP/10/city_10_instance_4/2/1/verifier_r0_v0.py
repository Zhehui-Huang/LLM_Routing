import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_positions):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check if tour includes exactly 8 cities
    if len(tour) != 9:
        return "FAIL"
    # Check if all cities in the tour other than the first and last are unique
    if len(set(tour[1:-1])) != len(tour[1:-1]):
        return "FAIL"
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    # Check if the calculated cost is approximately equal to the given total cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    return "CORRECT"

# Cities' coordinates
city_positions = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Given solution
tour_solution = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost_solution = 235.38

# Check the solution
result = verify_solution(tour_solution, total_travel_cost_solution, city_positions)
print(result)