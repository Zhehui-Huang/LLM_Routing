import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost):
    # Cities and their coordinates
    cities = {
        0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
        5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
    }
    
    # Requirements
    start_end_depot = tour[0] == 0 and tour[-1] == 0  # Tour must start and end at the depot city 0
    all_cities_once = len(set(tour)) == len(cities) and set(tour[:-1]) == set(cities.keys())  # Visit each city exactly once
    route_cost_correct = False  # Ensure cost is calculated correctly based on the provided tour
    
    # Calculate travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Compare provided cost with calculated cost
    route_cost_correct = math.isclose(calculated_cost, total_cost, rel_tol=1e-9)
    
    # Check all conditions
    if start_end_depot and all_cities_once and route_cost_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Tour provided
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
total_cost = 294.17253892411236

# Verify the tour
verification_result = verify_tour(tour, total_cost)
print(verification_result)