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

# Cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Example solution for verification purposes - these values must be calculated using a TSP solving method
sample_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
sample_total_cost = 500  # Example placeholder cost; in practice, compute the actual total cost

# Running the verification function
result = verify_solution(cities, sample_tour, sample_total_cost)
print(result)