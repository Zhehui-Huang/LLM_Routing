import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cost, cities):
    # Check if the tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at the depot city 0."
    
    # Check if all cities are visited exactly once except the depot
    if set(tour) != set(range(len(cities))):
        return False, "All cities must be visited exactly once."

    # Check the total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(cost, calculated_cost, rel_tol=1e-9):
        return False, f"Provided total cost {cost} does not match calculated cost {calculated_cost}."

    return True, "Tour and cost are correct."

# Provided example data
cities = [
    (53, 68), # depot city 0
    (75, 11), # city 1
    (91, 95), # city 2
    (22, 80), # city 3
    (18, 63), # city 4
    (54, 91), # city 5
    (70, 14), # city 6
    (97, 44), # city 7
    (17, 69), # city 8
    (95, 89)  # city 9
]

tour = [0, 5, 2, 9, 7, 1, 6, 4, 8, 3, 0]
total_travel_cost = 280.8414894850646

# Verification
is_correct, message = verify_tour(tour, total_travel_cost, cities)
if is_correct:
    print("CORRECT")
else:
    print("FAIL:", message)