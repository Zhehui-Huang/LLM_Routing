import math

# City coordinates provided in the problem
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Proposed solution
tour = [0, 8, 1, 9, 7, 2, 6, 3, 4, 5, 0]
total_cost = 466.79500612908856
max_distance = 75.28612089887484

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def validate_tour(tour, total_cost, max_distance):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (excluding the depot city which should be visited twice)
    if sorted(tour[1:-1]) != sorted(list(range(1, 10))):
        return "FAIL"
    
    # Calculate the actual total cost and the max distance
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i+1])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance
    
    # Compare computed cost and max distance to given values
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-5) or not math.isclose(computed_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run validation function
test_result = validate_tour(tour, total cost, max_distance)
print(test_result)