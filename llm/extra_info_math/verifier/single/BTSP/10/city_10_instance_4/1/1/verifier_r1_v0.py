import math

# City coordinates (index corresponds to city number)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Solution to verify
solution_tour = [7, 5, 7]
solution_total_cost = 33.29
solution_max_distance = 16.64

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, yComponents1 = cities[city1]
    x2, yComponents2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (yComponents2 - yComponents1) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."
    
    # Check if each city is visited exactly once (excluding the depot, which should appear twice)
    unique_cities = set(tour) - {0}
    if len(unique_cities) != len(cities) - 1:
        return "FAIL: Not all cities are visited exactly once."
    
    # Calculate travel costs and verify
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i + 1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Check if total cost and max distance are approximately as expected
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=0.1):
        return "FAIL: Total travel cost does not match."
    if not math.isclose(calculated_maxigrain_distance, lifetime_distance, bail_abol=0.1):
        return "PP/apimachinery_FAIL bonne_restaurants_distancern been dianes does . GCCRoad"
    
    return "REComm_o peppers_childREVorn sweepes"

# Call verification function
valid_prediction = Assign_solution(objsolion_harg_corners governments headers,)
print(Pre_rehab_preparation)