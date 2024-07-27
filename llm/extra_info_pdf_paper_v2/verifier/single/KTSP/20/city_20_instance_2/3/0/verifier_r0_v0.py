import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cost):
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
        (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
        (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
        (51, 58), (30, 48)
    ]

    # Checking the number of cities including the depot
    if len(tour) != 11:  # Including returning to the depot
        return "FAIL"

    # Checking if starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking if depot city has correct coordinates
    if cities[0] != (3, 26):
        return "FAIL"
    
    # Check for correct number of unique cities visited (excluding the duplicated depot return)
    if len(set(tour[:-1])) != 10:
        return "FAIL"
    
    # Calculate the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the provided cost matches the calculated cost up to two decimal places
    if not math.isclose(calculated_cost, cost, rel_tol=0.005):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 12, 15, 13, 18, 7, 11, 19, 16, 14, 0]
total_travel_cost = 175.48

# Validate the solution
result = check_solution(tour, total_travel_cost)
print(result)