import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    cities_coordinates = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }
    
    tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
    calculated_cost = 295.9919678938414

    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 10 or any(tour.count(city) != 1 for city in unique_cities if city != 0):
        return "FAIL"

    # Calculate total travel cost and compare
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])

    if not math.isclose(total_distance, calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Run the verification function and print the result
result = verify_solution()
print(result)