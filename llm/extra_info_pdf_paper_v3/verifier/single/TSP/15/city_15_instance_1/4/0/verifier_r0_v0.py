import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, total_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, excluding the depot
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Check the computed total travel cost with the solution's travel cost
    computed_cost = 0
    for i in range(len(tour)-1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if abs(computed_cost - total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Given cities' coordinates used for testing
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# The purported solution to verify (this should normally come from the problem solving logic)
# This is just example data, will go wrong unless explicitly calculated by actual solving algorithm
sample_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
sample_total_cost = 500  # Example cost, actual should be calculated

# Running the verification function
result = verify_solution(cities, sample_tour, sample_total_step_cost)
print(result)