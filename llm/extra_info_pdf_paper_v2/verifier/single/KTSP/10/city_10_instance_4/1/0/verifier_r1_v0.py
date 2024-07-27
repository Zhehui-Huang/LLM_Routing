import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_cost):
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    
    # [Requirement 1] The tour must start and end at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The robot can only visit exactly 8 cities, including the depot city.
    if len(set(tour)) != 8 + 1:
        return "FAIL"
    
    # [Requirement 5] The final output should list the city indices of the tour starting and ending at the depot city.
    if not all(city in tour for city in [0]):
        return "FAIL"
    
    # Calculate the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # [Requirement 4] The travel cost between any two cities is calculated using the Euclidean distance.
    # [Requirement 6] The final output should also include the total travel cost of the tour.
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# provided solution to be verified
tour = [0, 4, 7, 5, 1, 9, 8, 3, 0]
total_cost = 276.73548732934836

# Verifying the solution
result = verify_tour(tour, total_cost)
print(result)