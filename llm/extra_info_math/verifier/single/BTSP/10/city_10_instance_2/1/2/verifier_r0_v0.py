import math

# Provided solution details
tour = [0, 8, 2, 1, 9, 7, 6, 5, 0, 8, 0]
total_cost_provided = 406.8535
max_distance_provided = 67.1193

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Check Requirement 1: Start and end at depot city 0
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check Requirement 2: Each city must be visited exactly once (except depot)
def check_visit_once(tour):
    unique_cities = set(tour[1:-1]) # excluding the repeated depot at start and end
    return len(unique_cities) == 9 and all(city in unique_cities for city in range(1, 10))

# Check Requirement 3: Minimize max distance between consecutive cities
def check_max_distance(tour):
    consecutive_distances = [distance(tour[i], tour[i+1]) for i in range(len(tour)-1)]
    return max(consecutive_distances)

def unit_test():
    if not check_start_end(tour):
        return "FAIL"
    if not check_visit_once(tour):
        return "FAIL"
    if check_max_distance(tour) != max_distance_provided:
        return "FAIL"
    return "CORRECT"

result = unit_test()
print(f"Unit Test Result: {result}")