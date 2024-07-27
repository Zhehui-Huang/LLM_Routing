import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, expected_cost):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly 8 cities
    if len(set(tour)) != 9:  # 8 cities + 1 depot city
        return "FAIL"

    # Requirement 5: Correct format of the tour (implicitly checked by tour[0] and tour[-1])
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Requirement 3: Cost calculation method
    # Requirement 6: Outputs correct total travel cost
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define city coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Solution details
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]  # The proposed tour from the solution
total_travel_cost = 235.37735391753955  # The provided total cost

# Execute verification
result = verify_tour(tour, cities, total_travel_cost)
print(result)