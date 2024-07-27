import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Provide city coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    num_cities = len(cities)
    
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != num_cities - 1 or set(range(1, num_cities)) != unique_cities:
        return "FAIL"
    
    # Calculate the total cost based on the tour and compare with given total cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated cost matches the given total travel cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Tour from the solution
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_cost = 442.570870788815

# Check the solution
print(verify_solution(tour, total_cost))