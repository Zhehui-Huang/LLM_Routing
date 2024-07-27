import math

# City coordinates data
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Solution tour and total cost provided
tour = [0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
given_total_cost = 220.10

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_solution(tour, given_total_cost):
    # Verify the tour starts and ends at the depot
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Verify all cities are visited exactly once, excluding the depot
    unique_cities = set(tour[1:-1])  # exclude first and last city (depot)
    if len(unique_cities) != 14 or any(city not in unique_cities for city in range(1, 15)):
        return "FAIL"

    # Check if there are incorrect repetitions
    count_cities = {i: tour.count(i) for i in range(15)}
    if any(count > 1 for city, count in count_cities.items() if city != 0):
        return "FAIL"

    # Calculate total distance
    total_distance = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Verify if the total distance is below or equal to the given total cost
    if not math.isclose(total_distance, given_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run verification
result = verify_solution(tour, given_total_cost)
print(result)  # Output should be 'CORRECT' or 'FAIL'